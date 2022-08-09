from typing import List

from models.database.database import Session
from models.repos.mediasRepo import MediaRepo
from models.repos.mediaTypeRepo import MediaTypeRepo
from models.database.medias import Medias
from models.models.mediasModel import MediasModel
from models.database.mediaType import MediaType
from models.models.mediaTypeModel import MediaTypeModel


class MediaService:
    def __init__(self, app):
        _session = Session()
        self.app = app
        self.medias_repo = MediaRepo(_session, Medias)
        self.media_type_repo = MediaTypeRepo(_session, MediaType)

    def get_media_type(self) -> List[str]:
        self.media_type_repo.session = Session()
        result = []
        try:
            _media_type = self.media_type_repo.get_all()
            for _media in _media_type:
                model = MediaTypeModel.from_orm(_media)
                result.append(model.type)
        except Exception as ex:
            self.app.logger.error(f"Exception in get_media_type: {ex.args[0]}")
            result = []
            self.media_type_repo.session.rollback()
        self.media_type_repo.session.close()
        return result

    def new_media(self, media_name, media_type, id_user) -> MediasModel:
        self.medias_repo.session = Session()
        result = None
        id_type = self.__get_id_by_media_type(media_type)
        try:
            new_media: Medias = Medias(name=media_name,
                                       id_users=id_user,
                                       id_media_type=id_type)
            result = MediasModel.from_orm(self.medias_repo.insert(new_media))
        except Exception as ex:
            self.app.logger.error(f"Exception in new_media(): {ex.args[0]}")
            self.medias_repo.session.rollback()
        self.medias_repo.session.close()
        return result

    def get_list_medias_by_id_user(self, id_user) -> list[str]:
        self.medias_repo.session = Session()
        result = []
        try:
            all_media = self.medias_repo.get_all_filter(Medias.id_users == id_user)
            for _media in all_media:
                media_model = MediasModel.from_orm(_media)
                media_dict = {media_model.id: media_model.name}
                result.append(media_dict)
        except Exception as ex:
            self.app.logger.error(f"Exception in get_list_medias_name_by_id_user(): {ex.args[0]}")
            result = []
            self.medias_repo.session.rollback()
        self.medias_repo.session.close()
        return result

    def __get_id_by_media_type(self, media_type) -> int:
        self.media_type_repo.session = Session()
        result = -1
        try:
            media_type_model = MediaTypeModel.from_orm(self.media_type_repo.get_first(MediaType.type == media_type))
            result = media_type_model.id
        except:
            self.media_type_repo.session.rollback()
        self.media_type_repo.session.close()
        return result
