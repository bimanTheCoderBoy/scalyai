from datetime import datetime

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse

from config.security import verify_clerk_webhook
from container.app.dependencies import get_webhook_uow
from container.app.webhook_uow import WebhookUnitOfWork
from modules.webhook.application.dtos import WebhookEventDTO, WebhookEventStatus
from modules.webhook.domain.exceptions import (
    InvalidWebhookPayloadException,
    WebhookEventCreationFailedException,
)
from shared.logger import get_scaly_logger
import json

logger = get_scaly_logger(name=__name__)

router = APIRouter(prefix="/webhooks/clerk", tags=["webhooks"])


@router.post("/")
async def webhook_clerk(
    request: Request,
    uow: WebhookUnitOfWork = Depends(get_webhook_uow),
):
    payload = await request.body()
    headers = request.headers
    logger.info("webhook hit successfully")
    verified = verify_clerk_webhook(payload, headers)
    msg = json.loads(payload)
    logger.info(f"Verified payload type: {type(msg)}, value: {msg}")
    try:
        schema = WebhookEventDTO.model_validate(
            {
                "event_id": headers.get("svix-id"),
                "type": msg.get("type"),
                "event_timestamp": datetime.fromtimestamp(
                    msg.get("timestamp") / 1000
                ),
                "event_status": WebhookEventStatus.PENDING,
                "data": msg.get("data"),
            }
        )
    except Exception as e:
        logger.error(f"Invalid webhook payload: {e}")
        raise InvalidWebhookPayloadException()

    async with uow:
        await uow.webhook_service.ingest(schema)
        try:
            await uow.commit()
        except Exception:
            await uow.rollback()
            raise WebhookEventCreationFailedException()

    return JSONResponse(
        content="Webhook received and ingested",
        status_code=status.HTTP_202_ACCEPTED,
    )
