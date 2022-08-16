from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, DATE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Flux(Base):
    __tablename__ = "flux"

    id = Column(BIGINT(unsigned=True), primary_key=True)
    url = Column(String, nullable=False, unique=True)
    start_date = Column(DATE)
    end_date = Column(DATE)
    id_users = Column(BIGINT(unsigned=True))

