from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Static, TextArea


class Weather(Static):
    DEFAULT_CSS = """
    Weather {
        border-title-style: italic;
        border-title-align: center;
        border: round white;
        max_height: 60%;
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
        self.set_interval(1 / 60, self.update_weather)

    def update_weather(self):
        # resp = requests.get("https://wttr.in/blacksburg?1pQ")
        fake_text = '  \x1b[38;5;226m    \\   /    \x1b[0m Sunny\n  \x1b[38;5;226m     .-.     \x1b[0m \x1b[38;5;118m+57\x1b[0m(\x1b[38;5;082m53\x1b[0m) °F\x1b[0m     \n  \x1b[38;5;226m  ― (   ) ―  \x1b[0m \x1b[1m←\x1b[0m \x1b[38;5;226m9\x1b[0m mph\x1b[0m        \n  \x1b[38;5;226m     `-’     \x1b[0m 9 mi\x1b[0m           \n  \x1b[38;5;226m    /   \\    \x1b[0m 0.0 in\x1b[0m         \n                                                       ┌─────────────┐                                                       \n┌──────────────────────────────┬───────────────────────┤  Mon 25 Mar ├───────────────────────┬──────────────────────────────┐\n│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │\n├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤\n│ \x1b[38;5;226m    \\   /    \x1b[0m Sunny          │ \x1b[38;5;226m    \\   /    \x1b[0m Sunny          │ \x1b[38;5;226m    \\   /    \x1b[0m Sunny          │ \x1b[38;5;226m    \\   /    \x1b[0m Clear          │\n│ \x1b[38;5;226m     .-.     \x1b[0m \x1b[38;5;049m+35\x1b[0m(\x1b[38;5;050m32\x1b[0m) °F\x1b[0m     │ \x1b[38;5;226m     .-.     \x1b[0m \x1b[38;5;046m+48\x1b[0m(\x1b[38;5;047m44\x1b[0m) °F\x1b[0m     │ \x1b[38;5;226m     .-.     \x1b[0m \x1b[38;5;046m+48\x1b[0m(\x1b[38;5;047m44\x1b[0m) °F\x1b[0m     │ \x1b[38;5;226m     .-.     \x1b[0m \x1b[38;5;048m+39\x1b[0m(\x1b[38;5;049m35\x1b[0m) °F\x1b[0m     │\n│ \x1b[38;5;226m  ― (   ) ―  \x1b[0m \x1b[1m←\x1b[0m \x1b[38;5;118m3\x1b[0m-\x1b[38;5;154m4\x1b[0m mph\x1b[0m      │ \x1b[38;5;226m  ― (   ) ―  \x1b[0m \x1b[1m←\x1b[0m \x1b[38;5;190m7\x1b[0m-\x1b[38;5;226m8\x1b[0m mph\x1b[0m      │ \x1b[38;5;226m  ― (   ) ―  \x1b[0m \x1b[1m╮\x1b[0m \x1b[38;5;226m9\x1b[0m-\x1b[38;5;220m11\x1b[0m mph\x1b[0m     │ \x1b[38;5;226m  ― (   ) ―  \x1b[0m \x1b[1m╮\x1b[0m \x1b[38;5;154m5\x1b[0m-\x1b[38;5;220m11\x1b[0m mph\x1b[0m     │\n│ \x1b[38;5;226m     `-’     \x1b[0m 6 mi\x1b[0m           │ \x1b[38;5;226m     `-’     \x1b[0m 6 mi\x1b[0m           │ \x1b[38;5;226m     `-’     \x1b[0m 6 mi\x1b[0m           │ \x1b[38;5;226m     `-’     \x1b[0m 6 mi\x1b[0m           │\n│ \x1b[38;5;226m    /   \\    \x1b[0m 0.0 in | 0%\x1b[0m    │ \x1b[38;5;226m    /   \\    \x1b[0m 0.0 in | 0%\x1b[0m    │ \x1b[38;5;226m    /   \\    \x1b[0m 0.0 in | 0%\x1b[0m    │ \x1b[38;5;226m    /   \\    \x1b[0m 0.0 in | 0%\x1b[0m    │\n└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘\n\nFollow \x1b[46m\x1b[30m@igor_chubin\x1b[0m for wttr.in updates\n'
        self.text = fake_text

    def compose(self) -> ComposeResult:
        yield TextArea(self.text, soft_wrap=False, read_only=True)
