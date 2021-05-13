from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

engine = create_engine("sqlite+pysqlite:///db/app.db", future=True)
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

session = Session(engine)

def session_factory() -> Session:
    Base.metadata.create_all(engine)
    return _SessionFactory()