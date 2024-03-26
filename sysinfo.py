from textual.app import ComposeResult
from textual.widgets import Static
from block import Block

class Sysinfo(Static):
    DEFAULT_CSS = """
        Sysinfo {
            layout: grid;
            grid-size: 4 1;
            grid-gutter: 5;
            height: 10%;
            min-height: 7;
            align: center top;
            padding: 0 0 0 0;
            border: none;
        }
    """

    def compose(self) -> ComposeResult:
        yield Block(label="cpu", id="cpu")
        yield Block(label="mem")
        yield Block(label="disk")
        yield Block(label="active user")
