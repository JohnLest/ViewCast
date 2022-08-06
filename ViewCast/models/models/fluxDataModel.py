from pydantic import BaseModel


class FluxDataModel(BaseModel):
    id: int
    position: int
    time: int
    id_flux: int
    id_media: int

    class Config:
        orm_mode = True
