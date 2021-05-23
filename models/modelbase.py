import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

db_conn = os.getenv("DATABASE_URI")
if not db_conn:
    db_conn = "sqlite+pysqlite:///db/app.db"

engine = create_engine(db_conn, future=True)
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

session = Session(engine)

def session_factory() -> Session:
    Base.metadata.create_all(engine)
    return _SessionFactory()