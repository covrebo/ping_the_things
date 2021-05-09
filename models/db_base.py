from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("sqlite+pysqlite:///db/app.db", echo=True, future=True)

Base = declarative_base()

session = Session(engine)

def create_db():

    from models.host_models import Host

    Base.metadata.create_all(engine)

    return None