from pydantic import BaseModel, Field


class UsersModel(BaseModel):
    id_user: int = Field(alias="id")
    name: str
    mail: str
    password: str
    company: str
    location: str = None
    is_admin: bool = False
    path_media: str

    class Config:
        orm_mode = True
