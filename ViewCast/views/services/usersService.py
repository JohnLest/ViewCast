from sqlalchemy import and_
from models.database.database import Session
from models.repos.usersRepo import UsersRepo
from models.database.users import User


class UsersService:
    def __init__(self):
        _session = Session()
        self.users_repo = UsersRepo(_session, User)

    def connect(self, mail: str, psswd):
        self.users_repo.session = Session()
        try:
            user = self.users_repo.get_first(and_(User.mail == mail.lower(),
                                                 User.password == psswd))
        except:
            self.users_repo.session.rollback()
            self.users_repo.session.close()
            return "error"
        self.users_repo.session.close()
        return user
