from sqlalchemy import and_
from models.database.database import Session
from models.repos.usersRepo import UsersRepo
from models.database.users import User
from models.models.usersModel import UsersModel


class UsersService:
    def __init__(self, app):
        _session = Session()
        self.__users_repo = UsersRepo(_session, User)
        self.__app = app

    def connect(self, mail: str, psswd) -> UsersModel:
        self.__users_repo.session = Session()
        result = None
        try:
            user = self.__users_repo.get_first(and_(User.mail == mail.lower(),
                                                 User.password == psswd))
            result = UsersModel.from_orm(user)
        except:
            self.__users_repo.session.rollback()
        self.__users_repo.session.close()
        return result

    def check_admin(self, id_user) -> bool:
        self.__users_repo.session = Session()
        result = False
        try:
            user_model: UsersModel = UsersModel.from_orm(self.__users_repo.get_by_id(id_user))
            if user_model.is_admin:
                result = True
        except Exception as ex:
            self.__app.logger.error(f"Exception in check_admin(): {ex.args[0]}")
            result = False
            self.__users_repo.session.rollback()
        self.__users_repo.session.close()
        return result
