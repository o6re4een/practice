from services.countdown_manager import TimerWindow
from ui.information import Ui_MainWindow


class InformationWindow(TimerWindow, Ui_MainWindow):

    def __init__(self, main_app):
        super().__init__(target_time=main_app.target_time)

        self.setupUi(self)

        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        pass

    def update_countdown_label(self, text):
        """Обновление текста таймера на интерфейсе."""
        self.greet_time_left.setText(text)
