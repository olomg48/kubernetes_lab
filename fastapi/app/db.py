from sqlmodel import SQLModel, create_engine, Session
import os 

DATABASE_URL = os.getenv("DB_CONN")
engine = create_engine(DATABASE_URL, future=True)

def get_session():
    with Session(engine) as session:
        yield session

