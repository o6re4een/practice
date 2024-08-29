from services.app_sysyem_info import AppInfo
from services.countdown_manager import TimerWindow
from ui.greet_window import UiGreetWindow


class GreetWindow(TimerWindow, UiGreetWindow):
    def __init__(self, main_app):
        # Передаем целевую дату и время в базовый класс TimerWindow
        super().__init__(target_time="2024-10-10 10:25:00")
        self.setupUi(self)
        self.main_app = main_app
        self._app_info = AppInfo()
        self.init_ui()

    def init_ui(self):
        try:
            # Установка начальных значений в интерфейсе
            self.greet_date_label.setText(
                self._app_info.sys_time.strftime(
                    f"{self.get_day(self._app_info.sys_time.weekday())} %d {self.get_moth(self._app_info.sys_time.month)} %Y"
                )
            )

            # Пример переключения окна
            self.want_sponsor_btn.clicked.connect(self.swith_to_sponsor)
        except Exception as _e:
            print("Ошибка при инициализации: ", _e)

    def get_moth(self, month_num):
        moth_dict = {1: "Январь", 2: "Февраль", 8: "Август"}
        return moth_dict.get(month_num, "Неизвестный месяц")

    def get_day(self, day_num):
        day_dict = {
            0: "Понедельник",
            1: "Вторник",
            2: "Среда",
            3: "Четверг",
            4: "Пятница",
        }
        return day_dict.get(day_num, "Неизвестный день")

    def update_countdown_label(self, text):
        """Обновление текста таймера на интерфейсе."""
        self.greet_time_left.setText(text)

    def swith_to_sponsor(self):
        self.main_app.switch_window("Sponsor")

    def closeEvent(self, event):
        super().closeEvent(event)
