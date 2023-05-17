from dotenv import load_dotenv
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import Session, DeclarativeBase
import sqlalchemy as db
import os


load_dotenv()
engine = db.create_engine(f"postgresql+psycopg2://{os.environ['PG_USER']}:"
                          f"{os.environ['PG_PASSWORD']}@{os.environ['PG_HOST']}:"
                          f"5433/{os.environ['PG_DB']}"
                          )
metadata = MetaData()
session = Session(bind=engine)


class Base(DeclarativeBase):
    pass



class Images(Base):
    __table__ = Table('images', metadata, autoload_with=engine)