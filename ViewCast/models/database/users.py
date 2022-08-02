from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(BIGINT(unsigned=True), primary_key=True)
    name = Column(String, nullable=False, unique=True)
    mail = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String)
    is_admin = Column(BOOLEAN, nullable=False, default=0)
    path_media = Column(String, nullable=False, unique=True)
