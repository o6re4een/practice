import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

# Импорт расширенных окон
from services.confirm_sponsor_window import ConfirmSponosorWindow
from services.greet_window import GreetWindow
from services.information_window import InformationWindow
from services.sponsor_window import SponsorWindow


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()

        self.target_time = "2024-10-10 10:25:00"

        # Добавим отладочное сообщение для проверки инициализации
        print("Инициализация MainApp началась")
        try:
            # Создаем QStackedWidget для управления окнами
            self.stacked_widget = QStackedWidget()
            self.setCentralWidget(self.stacked_widget)

            # Добавляем все окна в QStackedWidget
            self.windows = {}
            self.add_window(GreetWindow(self), "Greet")
            self.add_window(SponsorWindow(self), "Sponsor")
            self.add_window(ConfirmSponosorWindow(self), "ConfirmSponsor")
            self.add_window(InformationWindow(self), "Information")

            # Устанавливаем начальное окно
            self.stacked_widget.setCurrentIndex(0)
            print("MainApp успешно инициализирован")

        except Exception as e:
            print(f"Ошибка при инициализации MainApp: {e}")

    def add_window(self, window, name):
        """Добавляет окно в QStackedWidget и сохраняет его по имени."""
        try:
            self.stacked_widget.addWidget(window)
            self.windows[name] = window
            print(f"Окно {name} добавлено успешно")
        except Exception as e:
            print(f"Ошибка при добавлении окна {name}: {e}")

    def switch_window(self, name):
        """Переключает на окно по имени."""
        try:
            if name in self.windows:

                self.stacked_widget.setCurrentWidget(self.windows[name])
                print(f"Переключено на окно: {name}")
            else:
                print(f"Окно {name} не найдено")
        except Exception as e:
            print(f"Ошибка при переключении на окно {name}: {e}")


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        main_app = MainApp()
        main_app.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
