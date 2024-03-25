from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Static
import requests

class Weather(Static):
    DEFAULT_CSS = """
    Weather {
        border-title-style: italic;
        border-title-align: center;
        border: round white;
    }
    """

    text = reactive("", recompose=True)

    def __init__(self,
                 name: str | None = None,
                 id: str | None = None,
                 classes: str | None = None,
                 disabled: bool = False):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)

    def on_mount(self):
        self.border_title = "Weather Report"
        self.update_weather()
        self.set_interval(30, self.update_weather)

    def update_weather(self):
        resp = requests.get("https://wttr.in/blacksburg?1pQ")
        self.text = resp.text

    def compose(self) -> ComposeResult:
        yield Static(self.text)