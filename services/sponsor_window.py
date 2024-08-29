import sys
from typing import Type
from services.countdown_manager import TimerWindow
from ui.sponsor_window import UISponsorWindow
from db import UserManager


class SponsorWindow(TimerWindow, UISponsorWindow):
    form_data: dict = {}

    def __init__(self, main_app):
        super().__init__(target_time="2024-10-10 10:25:00")
        self.setupUi(self)
        self.main_app = main_app
        self.init_ui()

    def init_ui(self):
        self.back_btn.clicked.connect(lambda: self.main_app.switch_window("Greet"))
        self.donate_sum_minus_btn.clicked.connect(self.minus_donate_sum)
        self.donate_sum_plus_btn.clicked.connect(self.plus_donate_sum)
        self.pay_btn.clicked.connect(self.submit_form)
        self.RunnerManager = UserManager()
        self.runners = self.get_runners()
        self.runner_list_inpt.addItems(self.runners)

        self.donate_sum_input.setText("50")
        self.donate_sum_label.setText("50")
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
        self.form_data["name"] = self.name_input.text()
        self.form_data["card_owner"] = self.card_owner_input.text()
        self.form_data["card_number"] = self.card_num_input.text()
        self.form_data["card_month"] = self.card_month_input.text()
        self.form_data["card_year"] = self.card_year_input.text()
        self.form_data["card_cvv"] = self.card_cvv_input.text()
        self.form_data["dontate_sum"] = self.dontate_sum_input.text()

    def submit_form(self):
        self.get_input_values()

    def minus_donate_sum(self):
        if int(self.donate_sum_input.text()) > 10:
            self.donate_sum_input.setText(str(int(self.donate_sum_input.text()) - 10))

    def plus_donate_sum(self):
        self.donate_sum_input.setText(str(int(self.donate_sum_input.text()) + 10))

    def update_donate_sum(self):
        donate_sum = self.donate_sum_input.text()
        self.donate_sum_label.setText(donate_sum)
