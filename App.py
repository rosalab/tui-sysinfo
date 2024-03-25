from textual.app import App, ComposeResult
from textual.widgets import Static
from sysinfo import Sysinfo

class TuiSysInfo(App):
    CSS_PATH = "tcss/app.tcss"

    def compose(self) -> ComposeResult:
        yield Sysinfo("One", classes="box-1")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")


if __name__ == "__main__":
    app = TuiSysInfo()
    app.run()
