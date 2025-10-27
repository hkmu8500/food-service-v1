from .core.cors_config import setup_cors
from .core.db_config import create_tables
from .core.exception_handlers import register_exception_handlers
from .core.fastapi_config import init_fastapi
from .utils.db_init import init_db
from .core.logger_config import setup_log_config
from .core.session_config import setup_session_config


app = init_fastapi()
setup_log_config()

setup_cors(app)
setup_session_config(app)



# Register the exception handler
register_exception_handlers(app)


# todo should use lifespan
@app.on_event("startup")
def on_startup():
    # Initialize database on startup
    create_tables()
    init_db()
