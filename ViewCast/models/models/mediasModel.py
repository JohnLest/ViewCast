from pydantic import BaseModel


class MediasModel(BaseModel):
    id: int
    name: str
    id_user: int
    id_type: int

    class Config:
        orm_mode = True
