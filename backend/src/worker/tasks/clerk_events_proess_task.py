import asyncio
from core.celery import celery_app
from core.logger import get_scaly_logger
from db.session import worker_session_factory
from core.redis import get_redis, init_redis, close_redis
from schemas.webhook_schema import WebhookEventDTO
from models.webhook_events import WebhookEventStatus
from repositories.webhook_repository import WebhookRepository
from repositories.cache.webhook_cache import WebhookCacheRepository
from repositories.user_repository import UserRepository
from services.webhook_service import WebhookService
from services.user_service import UserService
from events.handlers.clerk_user_handler import ClerkUserHandler

logger = get_scaly_logger(name=__name__)


@celery_app.task(
    bind=True,
    name="tasks.process_clerk_event",
    max_retries=5,
    acks_late=True, #if task crashes with giving Acknowledgement, it will be retried
)
def process_clerk_event(self, event_data: dict):
    asyncio.run(_process_clerk_event(self, event_data))


async def _process_clerk_event(task, event_data: dict):
    event = WebhookEventDTO.model_validate(event_data)
    logger.info(f"Event type: {event.type}, Event data keys: {event.data.keys()}")

    async with worker_session_factory() as session:
        try:
            await init_redis()
            redis = get_redis()
            webhook_repo = WebhookRepository(db=session)
            cache_repo = WebhookCacheRepository(cache=redis)
            user_repo = UserRepository(db=session)

            webhook_service = WebhookService(cache_repo=cache_repo, event_repo=webhook_repo)
            user_service = UserService(user_repo=user_repo)
            handler = ClerkUserHandler(user_service=user_service, webhook_service=webhook_service)

            await webhook_service.update_event_status(event.event_id, WebhookEventStatus.PROCESSING)
            success = await handler.handle(event)
            if not success:
                await webhook_service.update_event_status(event.event_id, WebhookEventStatus.SKIPPED)
            else:   
                await webhook_service.update_event_status(event.event_id, WebhookEventStatus.COMPLETED)

            await session.commit()
            logger.info(f"Successfully processed clerk event: {event.event_id}")
            
        except Exception as exc:
            await session.rollback()
            logger.error(f"Failed to process clerk event {event.event_id}: {exc}")

            await _mark_failed(event.event_id)

            backoff = 2 ** task.request.retries
            raise task.retry(exc=exc, countdown=backoff)
        finally:
            await close_redis()


async def _mark_failed(event_id: str):
    async with worker_session_factory() as session:
        try:
            webhook_repo = WebhookRepository(db=session)
            cache_repo = WebhookCacheRepository(cache=get_redis())
            webhook_service = WebhookService(cache_repo=cache_repo, event_repo=webhook_repo)
            await webhook_service.update_event_status(event_id, WebhookEventStatus.FAILED)
            await session.commit()
        except Exception as e:
            logger.error(f"Failed to mark event {event_id} as FAILED: {e}")
