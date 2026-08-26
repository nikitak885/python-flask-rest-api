from celery import Celery
import os

def create_celery():
    celery = Celery("python-flask-rest-api",
                     broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
                     backend=os.getenv("CELERY_BACKEND_URL", "redis://localhost:6379/0")
                     )
    return celery

celery = create_celery()