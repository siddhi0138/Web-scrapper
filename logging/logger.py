"""
Centralized logging configuration for the job market scraper.

Provides consistent logging across all modules with file and console output.
"""

import logging
import logging.handlers
from pathlib import Path


def setup_logger(name, log_level=logging.INFO):
    """
    Configure and return a logger instance.

    Args:
        name: Logger name (typically __name__)
        log_level: Logging level (default: INFO)

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Create logs directory if it doesn't exist
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)

    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        log_dir / "scraper.log",
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(log_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
