from sqlalchemy.orm import Session
from models.user import User

def test(db: Session):
    data = db.query(User).all()
    return data 