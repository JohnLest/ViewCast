from pydantic import BaseModel


class FluxModel(BaseModel):
    id: int
    url: str

    class Config:
        orm_mode = True
