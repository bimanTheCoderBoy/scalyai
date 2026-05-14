from svix.webhooks import Webhook, WebhookVerificationError
from core.exceptions.exceptions import WebHookInvalidSignatureException
from core.config import clerk_config

CLERK_WEBHOOK_SECRET = clerk_config.CLERK_WEBHOOK_SECRET

def verify_clerk_webhook(payload, headers):
    try:
        wh = Webhook(CLERK_WEBHOOK_SECRET)
        return wh.verify(payload, headers)
    except WebhookVerificationError:
        raise WebHookInvalidSignatureException()