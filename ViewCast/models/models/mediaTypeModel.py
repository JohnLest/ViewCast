from pydantic import BaseModel


class MediaTypeModel(BaseModel):
    id: int
    type: str

    class Config:
        orm_mode = True
