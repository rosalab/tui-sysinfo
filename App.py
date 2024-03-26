from textual.app import App, ComposeResult
from textual.widgets import Static
from sysinfos import SysInfos
from weather import Weather
from clocks import Clocks

class TuiSysInfo(App):
    DEFAULT_CSS = """
        Screen {
            layout: vertical;
        }
    """

    def compose(self) -> ComposeResult:
        # self.dark = False
        yield Clocks()
        yield SysInfos()
        yield Weather()

if __name__ == "__main__":
    app = TuiSysInfo()
    app.run()
