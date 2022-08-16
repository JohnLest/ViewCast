from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Medias(Base):
    __tablename__ = "medias"

    id = Column(BIGINT(unsigned=True), primary_key=True)
    name = Column(String, nullable=False)
    id_users = Column(BIGINT(unsigned=True), nullable=False)
    id_media_type = Column(SMALLINT(unsigned=True), nullable=False)
