import reflex as rx

from config import settings

config = rx.Config(
    app_name=settings.PROJECT_NAME,
    frontend_port=settings.FRONTEND_PORT,
    backend_port=settings.BACKEND_PORT,
    db_url=settings.DB_URL
)
