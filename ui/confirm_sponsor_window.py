import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class SponsorConfirmationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle('Marathon Skills 2016 – Sponsorship confirmation')
        self.setGeometry(100, 100, 600, 400)

        # Create main layout
        main_layout = QVBoxLayout()

        # Create and add back button
        back_button = QPushButton('Назад')
        back_button.setFixedWidth(100)
        back_button.setFixedHeight(30)
        back_layout = QHBoxLayout()
        back_layout.addWidget(back_button)
        back_layout.addStretch(1)
        main_layout.addLayout(back_layout)

        # Create and add title label
        title_label = QLabel('MARATHON SKILLS 2016')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        main_layout.addWidget(title_label)

        # Create and add thank you label
        thank_you_label = QLabel('Спасибо за вашу спонсорскую поддержку!')
        thank_you_label.setAlignment(Qt.AlignCenter)
        thank_you_label.setStyleSheet('font-size: 18px;')
        main_layout.addWidget(thank_you_label)

        # Create and add support label
        support_label = QLabel(
            'Спасибо за поддержку бегуна в Marathon Skills 2016!\nВаше пожертвование пойдет в его благотворительную организацию')
        support_label.setAlignment(Qt.AlignCenter)
        support_label.setStyleSheet('font-size: 14px;')
        main_layout.addWidget(support_label)

        # Create and add runner info label
        runner_info_label = QLabel('Иван Прудов(204) из Russia')
        runner_info_label.setAlignment(Qt.AlignCenter)
        runner_info_label.setStyleSheet('font-size: 16px;')
        main_layout.addWidget(runner_info_label)

        # Create and add organization label
        organization_label = QLabel('Фонд кошек')
        organization_label.setAlignment(Qt.AlignCenter)
        organization_label.setStyleSheet('font-size: 20px; font-weight: bold;')
        main_layout.addWidget(organization_label)

        # Create and add amount label
        amount_label = QLabel('$50')
        amount_label.setAlignment(Qt.AlignCenter)
        amount_label.setStyleSheet('font-size: 48px; font-weight: bold; color: gray;')
        main_layout.addWidget(amount_label)

        # Create and add back button at the bottom
        bottom_back_button = QPushButton('Назад')
        bottom_back_button.setFixedWidth(100)
        bottom_back_button.setFixedHeight(30)
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(bottom_back_button)
        bottom_layout.addStretch(1)
        main_layout.addLayout(bottom_layout)

        # Create and add countdown label
        countdown_label = QLabel('18 дней 8 часов и 17 минут до старта марафона!')
        countdown_label.setAlignment(Qt.AlignCenter)
        countdown_label.setStyleSheet('font-size: 12px; color: gray;')
        main_layout.addWidget(countdown_label)

        # Set main layout
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SponsorConfirmationWindow()
    ex.show()
    sys.exit(app.exec_())
