import datetime

from sqlalchemy import Column, Integer, String
from models.modelbase import Base


class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    date_created = Column(String, default=datetime.datetime.now())
    f_name = Column(String)
    l_name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"User(id={self.id}, name={self.f_name} {self.l_name}, email={self.email})"
