from svix.webhooks import Webhook, WebhookVerificationError
from shared.logger import get_scaly_logger
from config.settings import clerk_config
from modules.webhook.domain.exceptions import WebHookInvalidSignatureException

logger = get_scaly_logger(name=__name__)
def verify_clerk_webhook(payload, headers):
    try:
        wh = Webhook(clerk_config.CLERK_WEBHOOK_SECRET)
        return wh.verify(payload, headers)
    except WebhookVerificationError:
        raise WebHookInvalidSignatureException()
