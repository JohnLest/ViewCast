from ..database.database import Session
from ..dal.usersRepo import UsersRepo
from ..database.users import User



class UsersService:
    def __init__(self):
        _session = Session()
        self.user_repo = UsersRepo(_session, User)

    def get_all_user(self):
        self.user_repo.session = Session()
        try:
            result = self.user_repo.get_all()
        except:
            self.user_repo.session.rollback()
            self.user_repo.session.close()
            return "error"
        self.user_repo.session.close()
        return result
