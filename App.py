from textual.app import App, ComposeResult
from textual.widgets import Static
from sysinfo import Sysinfo
from weather import Weather

class TuiSysInfo(App):
    CSS_PATH = "tcss/app.tcss"

    def compose(self) -> ComposeResult:
        yield Sysinfo()
        yield Static("Three", classes="box")
        yield Weather()

if __name__ == "__main__":
    app = TuiSysInfo()
    app.run()
