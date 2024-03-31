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

        #all {
            layout: grid;
            grid-size: 1 2;
            grid-rows: 2fr 4.5fr;
        }
        
        #container {
            layout: grid;
            grid-size: 2;
            grid-columns: 6fr 1fr;
            background: $primary-background;
        }

        #container-top {
            layout: grid;
            grid-size: 2 1;
            grid-columns: 1fr 4fr;
            background: $primary-background-darken-3;
        }

        #clocksSys {
            layout: grid;
            grid-size: 1 2;
            grid-rows: 2fr 1fr;
            height: 100%;
        }

    """

    def compose(self) -> ComposeResult:
        yield Container (
            Container(
                Logo(),
                Container(
                    Clocks(),
                    SysInfos(),
                    id = "clocksSys"
                ),
                id = "container-top"
            ),
            Weather(),
            id = "all"
        )

if __name__ == "__main__":
    app = TuiSysInfo()
    app.run()
