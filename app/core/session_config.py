
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI
import os

# Enable signed cookie-based sessions
def setup_session_config(app: FastAPI):
    session_secret = os.environ.get("SESSION_SECRET", "change-me")
    app.add_middleware(SessionMiddleware, secret_key=session_secret, same_site="lax")
