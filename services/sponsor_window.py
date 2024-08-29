from datetime import datetime
import sys
from typing import Type
from services.countdown_manager import TimerWindow
from ui.sponsor_window import UISponsorWindow
from db import UserManager
from PyQt5.QtWidgets import QMessageBox


class SponsorWindow(TimerWindow, UISponsorWindow):
    form_data: dict = {}

    def __init__(self, main_app):
        super().__init__(target_time=main_app.target_time)
        self.setupUi(self)
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.back_btn.clicked.connect(lambda: self.main_app.switch_window("Greet"))
        self.donate_sum_minus_btn.clicked.connect(self.minus_donate_sum)
        self.donate_sum_plus_btn.clicked.connect(self.plus_donate_sum)
        self.pay_btn.clicked.connect(lambda: self.submit_form())
        self.RunnerManager = UserManager()
        self.runners = self.get_runners()
        self.runner_list_inpt.addItems(self.runners)

        self.donate_sum_input.setText("50")
        self.donate_sum_label.setText("50 $")
        self.donate_sum_input.textChanged.connect(self.update_donate_sum)

    def update_countdown_label(self, text):
        """Обновление текста таймера на интерфейсе."""
        self.greet_time_left.setText(text)

    def get_runners(self):

        runners = self.RunnerManager.get_runners()
        # print(runners[:10])
        runners = [
            f"{runner[0]} {runner[1]} - {runner[3]} ({runner[2]})" for runner in runners
        ]
        # print(runners[:10])
        return runners

    def get_input_values(self):
        self.form_data["name"] = self.lineEdit.text()
        self.form_data["card_owner"] = self.card_owner_input.text()
        self.form_data["card_number"] = self.card_num_input.text()
        self.form_data["card_month"] = self.card_month_input.text()
        self.form_data["card_year"] = self.card_year_input.text()
        self.form_data["card_cvv"] = self.card_cvv_input.text()
        self.form_data["donate_sum"] = self.donate_sum_input.text()
        self.form_data["sponsored_runner"] = self.runner_list_inpt.currentText()

    def submit_form(self):
        # if self.validate_data():
        self.get_input_values()
        self.main_app.windows["ConfirmSponsor"].update_data()
        self.main_app.switch_window("ConfirmSponsor")

    def validate_data(self):
        try:
            valid_card = (
                datetime.now().year - int(self.card_year_input.text()) > 0
                and int(self.card_month_input.text()) > 0
                and int(self.card_month_input.text()) < 13
            )
            valid_card = valid_card and len(self.card_num_input.text()) == 16
            valid_card = valid_card and len(self.card_cvv_input.text()) == 3
            valid_card = valid_card and len(self.donate_sum_input.text()) > 0
            valid_card = valid_card and self.runner_list_inpt.currentIndex() != 0
            return valid_card

        except Exception as _e:
            print("Ошибка валидации: ", _e)
            self.display_error(f"Некорректные данные \n {_e}")

            return False

    def display_error(self, message):
        MessageBox = QMessageBox()
        MessageBox.setText(message)
        MessageBox.exec()

    def minus_donate_sum(self):
        if int(self.donate_sum_input.text()) > 10:
            self.donate_sum_input.setText(str(int(self.donate_sum_input.text()) - 10))

    def plus_donate_sum(self):
        self.donate_sum_input.setText(str(int(self.donate_sum_input.text()) + 10))

    def update_donate_sum(self):
        donate_sum = self.donate_sum_input.text()
        self.donate_sum_label.setText(donate_sum + " $")
