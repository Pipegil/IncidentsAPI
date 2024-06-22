from firestorefastapi.daos.login import LoginDAO

login_dao = LoginDAO()


class LoginService:
    def verify_user(self, email: str, password: str):
        return login_dao.verify(email, password)
