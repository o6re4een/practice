import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel


class TWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Window")
        self.setGeometry(100, 100, 800, 600)
        label = QLabel("This is a test window", self)
        label.setGeometry(50, 50, 200, 50)


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()

        print("Инициализация MainApp началась")
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.windows = {}
        # Добавляем временное тестовое окно вместо дочерних классов
        self.add_window(TWindow(), "test_window")
        self.stacked_widget.setCurrentIndex(0)
        print("MainApp успешно инициализирован")

    def add_window(self, window, name):
        """Добавляет окно в QStackedWidget и сохраняет его по имени."""
        self.stacked_widget.addWidget(window)
        self.windows[name] = window
        print(f"Окно {name} добавлено успешно")

    def switch_window(self, name):
        """Переключает на окно по имени."""
        if name in self.windows:
            self.stacked_widget.setCurrentWidget(self.windows[name])
            print(f"Переключено на окно: {name}")


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        main_app = MainApp()
        main_app.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
