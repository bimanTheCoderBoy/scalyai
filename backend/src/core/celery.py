from celery import Celery
from kombu import Queue
from core.config import celery_config

celery_app = Celery(
    "scalyai",
    broker=celery_config.CELERY_BROKER_URL,
    backend=celery_config.CELERY_RESULT_BACKEND,
    include=["worker.tasks.clerk_events_proess_task"],
)

# Define queues
celery_app.conf.task_queues = (
    Queue("clerk_events"),
)

# Route tasks to queues
celery_app.conf.task_routes = {
    "tasks.process_clerk_event": {"queue": "clerk_events"},
}