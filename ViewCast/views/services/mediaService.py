from models.database.database import Session
from models.repos.mediasRepo import MediaRepo
from models.repos.mediaTypeRepo import MediaTypeRepo
from models.database.medias import Medias
from models.database.mediaType import MediaType


class MediaService:
    def __init__(self):
        _session = Session()
        self.medias_repo = MediaRepo(_session, Medias)
        self.media_type_repo = MediaTypeRepo(_session, MediaType)

    def get_media_type(self):
        self.media_type_repo.session = Session()
        result = []
        try:
            _media_type = self.media_type_repo.get_all()
            for _media in _media_type:
                result.append(_media.type)
        except:
            self.media_type_repo.session.rollback()
            self.media_type_repo.session.close()
            return None
        return result

    def new_media(self, media_name, media_type, id_user):
        self.medias_repo.session = Session()
        id_type = self.get_id_by_media_type(media_type)
        try:
            new_media: Medias = Medias(name= media_name,
                                       id_users=id_user,
                                       id_media_type=id_type)
            return self.medias_repo.insert(new_media)
        except:
            self.medias_repo.session.rollback()
            self.medias_repo.session.close()
            return None

    def get_id_by_media_type(self, media_type):
        self.media_type_repo.session = Session()
        try:
            _media_type: MediaType = self.media_type_repo.get_first(MediaType.type == media_type)
            return _media_type.id
        except:
            self.media_type_repo.session.rollback()
            self.media_type_repo.session.close()
            return None
