from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import SMALLINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VFlux(Base):
    __tablename__ = "v_flux"

    url = Column(String, primary_key=True)
    media = Column(String)
    position = Column(SMALLINT(unsigned=True), primary_key=True)
    time = Column(SMALLINT(unsigned=True))
