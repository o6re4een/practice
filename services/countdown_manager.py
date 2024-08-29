from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from datetime import datetime
import time


class CountdownThread(QThread):
    """Класс потока для отсчета времени."""

    update_countdown = pyqtSignal(str)

    def __init__(self, target_time):
        super().__init__()
        self.target_time = target_time
        self.timer_enabled = True

    def run(self):
        target_date = datetime.strptime(self.target_time, "%Y-%m-%d %H:%M:%S")

        while self.timer_enabled:
            now = datetime.now()
            time_difference = target_date - now
            days = time_difference.days
            hours, remainder = divmod(time_difference.seconds, 3600)
            minutes = remainder // 60
            seconds = remainder % 60

            self.update_countdown.emit(
                f"{days} дней {hours} часов и {minutes} минут и {seconds} секунд до события!"
            )

            time.sleep(1)  # Обновление каждую секунду

    def stop(self):
        self.timer_enabled = False
        self.terminate()


class TimerWindow(QMainWindow):
    """Базовый класс окна с поддержкой таймера."""

    def __init__(self, target_time):
        super().__init__()
        self.target_time = target_time
        self.countdown_thread = None
        self.init_timer()

    def init_timer(self):
        """Инициализация таймера."""
        self.countdown_thread = CountdownThread(self.target_time)
        self.countdown_thread.update_countdown.connect(self.update_countdown_label)
        self.countdown_thread.start()

    def update_countdown_label(self, text):
        """Метод для обновления интерфейса — должен быть переопределен в наследниках."""
        # Этот метод можно переопределить в дочерних классах для обновления интерфейса
        print(text)

    def closeEvent(self, event):
        """Остановка таймера при закрытии окна."""
        if self.countdown_thread and self.countdown_thread.isRunning():
            self.countdown_thread.stop()
            self.countdown_thread.wait()
        super().closeEvent(event)
