"""Provides utilities for setting up logging configurations.

Retrieves logger instances for different parts of the application.
"""

from __future__ import annotations

import logging

from rich.console import Console
from rich.logging import RichHandler

console = Console()

def setup_logging(level: int = logging.INFO) -> None:
    """Set up logging with Rich handler for prettier output."""
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, rich_tracebacks=True)],
    )

def get_logger(name: str) -> logging.Logger:
    """Get a logger instance."""
    return logging.getLogger(name)
