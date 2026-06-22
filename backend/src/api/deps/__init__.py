from core.redis import get_redis
from api.deps.uow.webhook_uow import WebhookUnitOfWork


def get_webhook_uow() -> WebhookUnitOfWork:
    return WebhookUnitOfWork(redis=get_redis())

from fastapi import Depends, HTTPException, status, Request

def get_current_user(request: Request):
    user = request.state.user  # set by middleware

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )

    return user