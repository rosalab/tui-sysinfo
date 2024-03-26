from textual.app import App, ComposeResult

from view.clocks import Clocks
from view.sysinfos import SysInfos
from view.weather import Weather


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
