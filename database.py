from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base # orm modles create panna 
from sqlalchemy.orm import sessionmaker # it will create session to talk to database 
import os # to read environment variables env filesaaaa
from dotenv import load_dotenv # you can use env that database url daa .

load_dotenv() 
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
