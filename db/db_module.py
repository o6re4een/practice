import os

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from functools import wraps
from dotenv import load_dotenv
import logging

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)

logging.basicConfig(level=logging.INFO)


# Декоратор для управления сессией
def session_manager(session_factory):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):  # Первый аргумент - self (экземпляр класса)
            session = session_factory()  # Создание сессии
            try:
                # Вызов декорированного метода с передачей self и session
                result = func(self, session, *args, **kwargs)
                session.commit()  # Коммит транзакции, если всё прошло успешно
                return result
            except SQLAlchemyError as e:
                session.rollback()  # Откат транзакции в случае ошибки
                logging.error(f"Database error occurred: {e}")
                raise  # Повторное возбуждение исключения
            finally:
                session.close()  # Закрытие сессии

        return wrapper

    return decorator


# def app():
#     with engine.connect() as conn:
#         stmt = text("select * from staff")
#         print(conn.execute(stmt).fetchall())
