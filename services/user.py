# from fastapi import FastAPI, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from fastapi.responses import JSONResponse
# from main import connetion

# database = Session = Depends(connetion)

def get_all_users():
    # Your logic to get user info, e.g., from a database
    return { "name": "John Doe"}