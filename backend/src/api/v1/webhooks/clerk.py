from fastapi import APIRouter
from fastapi import Request
from core.logger import get_scaly_logger
logger = get_scaly_logger(name=__name__)


router = APIRouter(prefix="/webhooks/clerk", tags=["webhooks"])

@router.post("/")
async def webhook_clerk(request: Request):
    logger.info("Webhook received")
    return {"message": "Webhook received"}