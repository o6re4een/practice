from services.countdown_manager import TimerWindow
from ui.confirm_sponsor_window import Ui_MainWindow
from PyQt5.QtWidgets import qApp


class ConfirmSponosorWindow(TimerWindow, Ui_MainWindow):

    def __init__(self, main_app):
        super().__init__(target_time=main_app.target_time)

        self.setupUi(self)
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.pushButton.clicked.connect(lambda: self.main_app.switch_window("Greet"))
        self.pushButton_2.clicked.connect(lambda: self.main_app.switch_window("Greet"))

    def update_countdown_label(self, text):
        """Обновление текста таймера на интерфейсе."""
        self.bottom.setText(text)

    def update_data(self):
        self.label_3.setText(
            self.main_app.windows["Sponsor"].form_data["sponsored_runner"]
        )
        self.label_5.setText(self.main_app.windows["Sponsor"].form_data["donate_sum"])
