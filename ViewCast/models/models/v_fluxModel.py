from pydantic import BaseModel


class VFluxModel(BaseModel):
    url: str
    media: str
    position: int
    time: int

    class Config:
        orm_mode = True
