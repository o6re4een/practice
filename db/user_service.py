from sqlalchemy import text
from db import Session, session_manager
from db import User


class UserManager:
    def __init__(self):
        pass

    @session_manager(Session)
    def get_all_users(self, session):
        # Используем session для работы с базой данных
        users = session.query(User).all()
        return users

    @session_manager(Session)
    def add_user(self, session, username, email):
        new_user = User(username=username, email=email)
        session.add(new_user)
        # session.commit() будет вызвано автоматически декоратором
        return new_user

    @session_manager(Session)
    def get_runners(self, session):
        query = text(
            "Select user.FirstName, user.LastName, runner.CountryCode, runner.RunnerId from country inner join runner on country.CountryCode = runner.CountryCode inner join user on runner.Email = user.Email"
        )

        runners = session.execute(query)
        runners = [runner for runner in runners]
        # print(runners)
        return runners


# Пример использования класса
# manager = UserManager("Admin")

# # Получение всех пользователей
# users = manager.get_runners()
