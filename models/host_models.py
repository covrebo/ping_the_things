import datetime

from sqlalchemy import Column, Integer, String
from models.modelbase import Base


class Host(Base):
    __tablename__ = "host_table"

    id = Column(Integer, primary_key=True)
    date_created = Column(String, default=datetime.datetime.now())
    host = Column(String)
    host_name = Column(String)

    def __repr__(self):
        return f"Host(id={self.id}, host={self.host}, host_name={self.host_name})"
