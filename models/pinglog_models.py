import datetime

from sqlalchemy import Column, Integer, String, Boolean
from models.modelbase import Base


class PingLog(Base):
    __tablename__ = "ping_log"

    id = Column(Integer, primary_key=True)
    date_created = Column(String, default=datetime.datetime.now())
    batch = Column(Integer, default=1)
    host = Column(String)
    host_name = Column(String)
    status = Column(Boolean)

    def __repr__(self):
        return f"Ping Log Entry(id={self.id}, batch={self.batch}, host={self.host}, host_name={self.host_name}, status={self.status})"
