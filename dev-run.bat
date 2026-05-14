@echo off
start "Frontend" cmd /k "cd /d frontend && npm run dev"
start "Backend"  cmd /k "cd /d backend && .venv\Scripts\activate && langgraph dev"
start "Celery"   cmd /k "cd /d backend\src && ..\.venv\Scripts\activate && celery -A core.celery:celery_app worker --queues=clerk_events --loglevel=info --pool=solo"