from textual.app import App, ComposeResult
from textual.widgets import Static, Digits
from textual.containers import Container


class Block(Static):
    DEFAULT_CSS = """
        #container {
            layout: grid;
            grid-size: 1 2;
        }

        .title {
            content-align-horizontal: center;
            content-align-vertical: middle;
            height: 10%
        }
    """

    def compose(self) -> ComposeResult:
        yield Container(
            Static("CPUINFO", classes="title"),
            Digits("100%"),
            id="container",
        )
