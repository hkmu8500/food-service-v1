from .core.cors_config import setup_cors
from .core.exception_handlers import register_exception_handlers
from .core.fastapi_config import init_fastapi

app = init_fastapi()

setup_cors(app)

# Register the exception handler
register_exception_handlers(app)
