from .core.cors_config import setup_cors
from .core.db_config import create_tables
from .core.exception_handlers import register_exception_handlers
from .core.fastapi_config import init_fastapi
from .utils.db_init import init_db

app = init_fastapi()

setup_cors(app)

# Register the exception handler
register_exception_handlers(app)


'''
Why comment the init db operation?
There  is a wired issue on_event annotation and lifespan, these events notification occassionally not working in serverless
cloud like "Vercel".
Base on above situation, the init_db() will execute in possible case, when it executed, it will panic caused by the primary key conflict.
So, we comment the init_db() operation, If you want to init the db, please call admin router "/api/admin/table/refreshAll".
'''
@app.on_event("startup")
def on_startup():
    # Initialize database on startup
    # create_tables()
    # init_db()
    None
