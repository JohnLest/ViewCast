from pydantic import BaseModel


class MediasModel(BaseModel):
    id: int
    name: str
    id_users: int
    id_media_type: int

    class Config:
        orm_mode = True
