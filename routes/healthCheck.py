from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from main import connetion

router = APIRouter()

@router.get("/health", tags=["Health Check"])
def health_check(db: Session = Depends(connetion)):
    try:
        # Execute a simple query to check the connection
        db.execute('SELECT 1')
        return {"status": "Database connected successfully!"}
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Failed to connect to the database.")