# src/interfaces/api/main.py
from fastapi import FastAPI
from src.utils.logger import get_logger
from src.utils.exceptions import EduFlowError, eduflow_exception_handler
from src.interfaces.api import students, teachers, courses, enrollments, scraped  # ✅ add scraped

logger = get_logger(__name__)

app = FastAPI(title="EduFlow SMS", version="1.0.0")

# Register routers
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(teachers.router, prefix="/teachers", tags=["Teachers"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["Enrollments"])
app.include_router(scraped.router, prefix="/resources", tags=["Scraped Resources"])  # ✅ add here

# Exception handler
app.add_exception_handler(EduFlowError, eduflow_exception_handler)


@app.get("/health")
async def health_check():
    logger.info("Health check requested")
    return {"status": "ok"}
