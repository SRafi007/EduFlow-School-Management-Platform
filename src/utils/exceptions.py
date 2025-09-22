# src/utils/exceptions.py
from fastapi import Request
from fastapi.responses import JSONResponse
from src.utils.logger import get_logger

logger = get_logger(__name__)


class EduFlowError(Exception):
    """Base exception for the EduFlow system."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class DatabaseError(EduFlowError):
    """Raised when database operations fail."""


class ScraperError(EduFlowError):
    """Raised for scraper-related failures."""


class BusinessRuleViolation(EduFlowError):
    """Raised when business rules (e.g., enrollment) are violated."""


# FastAPI-compatible handler
async def eduflow_exception_handler(request: Request, exc: EduFlowError):
    logger.error(
        f"EduFlowError: {exc.message} | Path: {request.url.path} | Method: {request.method}"
    )
    return JSONResponse(
        status_code=400,
        content={"error": exc.__class__.__name__, "message": exc.message},
    )
