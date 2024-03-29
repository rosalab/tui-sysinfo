from textual.app import App, ComposeResult

from view.clocks import Clocks
from view.sysinfos import SysInfos
from view.weather import Weather
from widgets.logo import Logo
from textual.containers import Container

class TuiSysInfo(App):
    DEFAULT_CSS = """
        Screen {
            layout: vertical;
        }

        #container {
            layout: grid;
            grid-size: 2;
            grid-columns: 4fr 1fr;
            background: $primary-lighten-1;
        }
    """

    def compose(self) -> ComposeResult:
        # self.dark = False
        yield Clocks()
        yield SysInfos()
        yield Container(
            Weather(),
            Logo(),
            id = "container"
        )


if __name__ == "__main__":
    app = TuiSysInfo()
    app.run()
