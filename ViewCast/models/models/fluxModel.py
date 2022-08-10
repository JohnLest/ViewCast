from pydantic import BaseModel
from datetime import datetime


class FluxModel(BaseModel):
    id: int
    url: str
    start_date: datetime = None
    end_date: datetime = None
    id_users: int

    class Config:
        orm_mode = True


class FluxShowModel(BaseModel):
    url: str
    cover: str = None
    start_date: datetime = None
    end_date: datetime = None

    class Config:
        orm_mode = True
