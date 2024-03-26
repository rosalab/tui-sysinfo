import requests
from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Static


def get_weather_data():
    resp = requests.get("https://wttr.in/blacksburg?2dT")
    return "\n".join(resp.text.splitlines()[:-3])


class Weather(Static):
    DEFAULT_CSS = """
    Weather {
        border-title-style: italic;
        border-title-align: center;
        border: round white;
        text-align: center;
        width: 100%;
        max-height: 70%;
        color: auto;
    }
    """

    text = reactive(get_weather_data)

    def __init__(self,
                 name: str | None = None,
                 id: str | None = None,
                 classes: str | None = None,
                 disabled: bool = False):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)

    def on_mount(self):
        self.border_title = "Weather Report"
        self.set_interval(30, self.update_weather)

    def update_weather(self):
        self.text = get_weather_data()

    def watch_text(self):
        try:
            self.query_one(Static).update(self.text)
        except Exception as e:
            pass

    def compose(self) -> ComposeResult:
        yield Static(self.text)
