from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from ui.greet_window import UiGreetWindow
from ui.sponsor_window import UISponsorWindow


class ContentManager:
    def __init__(self, layout):
        self.layout = layout
        self.windows = {
            "Start_Window": uic.loadUi("ui/greet.ui"),
            "Sponsor_Window": uic.loadUi("ui/sponsor.ui")
        }

    def show_content(self, name):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if (child.widget()):
                child.widget().deleteLater()
        window: QMainWindow = self.windows.get(name)
        if window:
            if hasattr(window, "window_content"):
                content_widget = window.window_content
            else:
                content_widget = window.centralWidget()
                print(content_widget)
            self.layout.addWidget(content_widget)
