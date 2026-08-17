from fastapi import FastAPI
from app.api.employee import router as employee_router
import app.models
from app.core.exceptions.exception_handlers import app_exception_handler
from app.core.exceptions.exceptions import AppException

app = FastAPI(
    title="Employee Task Manager API",
    version="1.0.0",
)

app.add_exception_handler(
    AppException,
    app_exception_handler,
)

app.include_router(employee_router)


@app.get("/")
def root():
    return {"message": "Welcome to the Employee Task Manager API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}




