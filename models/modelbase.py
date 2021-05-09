from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

engine = create_engine("sqlite+pysqlite:///db/app.db", echo=True, future=True)
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

session = Session(engine)

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()

# def create_db():
#
#     from models.host_models import Host
#
#     Base.metadata.create_all(engine)
#
#     return None