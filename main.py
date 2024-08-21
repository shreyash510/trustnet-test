import uvicorn
from fastapi import FastAPI,  Depends, HTTPException, status


from routes import user

# from .database.connection import SessionLocal, engine

app = FastAPI()

# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


app = FastAPI()

app.include_router( user.router, prefix="/api/v1")
# app.include_router(another_module_routes.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)