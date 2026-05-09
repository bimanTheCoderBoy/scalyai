from svix.webhooks import Webhook, WebhookVerificationError
from core.exceptions.exceptions import WebHookInvalidSignatureException

CLERK_WEBHOOK_SECRET = "your_secret"

def verify_clerk_webhook(payload, headers):
    try:
        wh = Webhook(CLERK_WEBHOOK_SECRET)
        return wh.verify(payload, headers)
    except WebhookVerificationError:
        raise WebHookInvalidSignatureException()