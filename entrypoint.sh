#!/bin/bash
alembic upgrade head
uvicorn app.server:app --reload --host 0.0.0.0 --port 5000