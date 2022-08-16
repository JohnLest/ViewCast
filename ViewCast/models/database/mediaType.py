from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MediaType(Base):
    __tablename__ = "media_type"

    id = Column(SMALLINT(unsigned=True), primary_key=True)
    type = Column(String, unique=True)
