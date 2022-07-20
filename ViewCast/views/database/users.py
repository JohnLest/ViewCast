from sqlalchemy import Column, String, BIGINT, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key = True)
    name = Column(String)
    mail = Column(String)
    password = Column(String)
    company = Column(String)
    location = Column(String)
    is_admin = Column(BOOLEAN)
