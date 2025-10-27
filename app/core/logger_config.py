

import logging
import logging.config

# Configure application logging so route loggers emit INFO messages
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"}
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "default"}
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        # Align server logs and keep SQLAlchemy engine noise down
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"level": "INFO"},
        "sqlalchemy.engine": {"level": "WARNING"},
    },
}


def setup_log_config():
    logging.config.dictConfig(LOGGING)
