# src/utils/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler
from src.config.settings import settings


def get_logger(name: str) -> logging.Logger:
    """Returns a configured logger with console + file handlers."""
    logger = logging.getLogger(name)

    if logger.hasHandlers():  # Avoid duplicate handlers
        return logger

    logger.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))

    # Ensure logs directory exists
    log_dir = os.path.dirname(settings.log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # File handler (rotating logs: 5MB, keep 3 backups)
    file_handler = RotatingFileHandler(
        settings.log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False

    return logger


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("🚀 EduFlow SMS is starting...")
    logger.debug(f"Running in debug={settings.debug}, DB={settings.database_url}")
    logger.info("Health check requested")
