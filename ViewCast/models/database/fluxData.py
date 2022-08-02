from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FluxData(Base):
    __tablename__ = "flux_data"

    id = Column(BIGINT(unsigned=True), primary_key=True)
    position = Column(SMALLINT(unsigned=True), nullable=False,)
    time = Column(SMALLINT(unsigned=True), nullable=False)
    id_flux = Column(BIGINT(unsigned=True), nullable=False)
    id_media = Column(BIGINT(unsigned=True), nullable=False)
