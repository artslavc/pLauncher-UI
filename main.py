import webview
import sys
import os

class Api:
    """API WebView"""
    def __init__(self):
        print("✅ API инициализирован")
        self._window = None
    
    def set_window(self, window):
        """Ссылка на окно после его создания"""
        self._window = window

def create_window():
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    index_path = os.path.join(base_path, "templates", "index.html") # Точка Входа

    api = Api()

    window = webview.create_window(
        "pLauncherr",
        url=f"file:///{index_path}",
        js_api=api,
        width=1272,
        height=874,
        resizable=False,
        frameless=False,
        background_color="#000000"
    )

    api.set_window(window)

    webview.start()


if __name__ == "__main__":
    create_window()