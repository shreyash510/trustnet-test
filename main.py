import uvicorn
import logging

from fastapi import FastAPI,  Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import text 
from services import test

from routes import user

from database.connection import SessionLocal, engine

app = FastAPI()

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 

@app.get("/health", tags=["Health Check"])
def health_check(db: Session = Depends(get_db)):
    try:
        # Execute a simple query to check the connection
        db.execute(text("SELECT 1"))
        return {"status": "Database connected successfully!"}
    except SQLAlchemyError as e:
        # Log the error message
        logger.error(f"Database connection failed: {str(e)}")
        raise HTTPException(status_code=503, detail=f"Failed to connect to the database: {str(e)}")


@app.get("/test")
def test_get(db: Session = Depends(get_db)):
    db_user = test.test(db)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User not found")


app.include_router( user.router, prefix="/api/v1")
# app.include_router( healthCheck.router, prefix="/api/v1/health")
# app.include_router(another_module_routes.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)