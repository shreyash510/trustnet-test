from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres.qkqembjayekrveiggapk:F4RmMHQdVXSvgBj@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"
# postgresql://postgres.qkqembjayekrveiggapk:[YOUR-PASSWORD]@aws-0-ap-south-1.pooler.supabase.com:5432/postgres
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()