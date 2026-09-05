@echo off
start "Frontend" cmd /k "cd /d frontend && npm run dev"
start "Backend"  cmd /k "cd /d server\src && ..\.venv\Scripts\activate && uvicorn main:app --reload --host 0.0.0.0 --port 8000"
start "TaskIQ Worker" cmd /k "cd /d server\src && ..\.venv\Scripts\activate && taskiq worker config.taskiq:broker --reload"
start "redis & postgres with docker compose" cmd /k "cd /d . && docker compose up -d"
