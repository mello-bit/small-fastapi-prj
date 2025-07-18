from sqlmodel import SQLModel, Session
from api.db.config import DATABASE_URL
import sqlmodel


if DATABASE_URL == "":
    raise NotImplementedError("Provide database url to the .env file!!")

print(DATABASE_URL)
engine = sqlmodel.create_engine(DATABASE_URL)



def init_db():
    print("Creating database...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session