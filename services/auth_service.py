import dataclasses


@dataclasses.dataclass
class AuthInfo:
    email: str
    password: str


class AuthService:
    def __init__(self):
        pass

    def login(self, user_data: AuthInfo):
        pass

    def logout(self):
        pass
