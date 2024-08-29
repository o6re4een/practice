import datetime

from sqlalchemy import select

from db.db_module import session_manager, Session
from db.models import Event


class AppInfo:
    marathon_start_time = 0
    sys_time: datetime.datetime

    def __init__(self):
        self.sys_time = self.get_time_now()
        self.days_left = 0

    @session_manager(Session)
    def get_mh_time(self, session, marathon_id: str | None):
        if not marathon_id:
            return datetime.datetime.strptime("2024-12-10 16:00", "'%Y-%m-%d %H:%M'")
        stmt = select(Event.StartDateTime).where(Event.EventId.is_(marathon_id))
        return session.execute(stmt).one()

    @staticmethod
    def get_time_now():
        return datetime.datetime.now()
