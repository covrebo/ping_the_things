from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite+pysqlite:///db/app.db", echo=True, future=True)

Base = declarative_base()

def create_db():

    from models.host_models import Host

    Base.metadata.create_all(engine)

    return None