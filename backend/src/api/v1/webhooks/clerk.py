from fastapi import APIRouter, Request, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from core.logger import get_scaly_logger
from core.security import verify_clerk_webhook
from schemas.webhook_schema import WebhookEventDTO, WebhookEventStatus
from core.exceptions.exceptions import InvalidWebhookPayloadException, WebhookEventCreationFailedException
from api.deps import get_webhook_service, get_db
from services.webhook_service import WebhookService
from datetime import datetime

logger = get_scaly_logger(name=__name__)

router = APIRouter(prefix="/webhooks/clerk", tags=["webhooks"])

@router.post("/")
async def webhook_clerk(
    request: Request,
    webhook_service: WebhookService = Depends(get_webhook_service),
    db: AsyncSession = Depends(get_db),
):
    payload = await request.body()
    headers = request.headers

    verified = verify_clerk_webhook(payload, headers)

    try:
        schema = WebhookEventDTO.model_validate(
            {
                "event_id": verified.get("instance_id"),
                "type": verified.get("type"),
                "event_timestamp": datetime.fromtimestamp(verified.get("timestamp") / 1000),
                "event_status": WebhookEventStatus.PENDING,
                "data": verified.get("data")
            }
        )
    except Exception:
        raise InvalidWebhookPayloadException()

    await webhook_service.ingest(schema)

    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise WebhookEventCreationFailedException()

    return JSONResponse(content="Webhook received and ingested", status_code=status.HTTP_202_ACCEPTED)
