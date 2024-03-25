from textual import events
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static
from block import Block

class Sysinfo(Static):
    DEFAULT_CSS = """
        Sysinfo {
            layout: grid;
            grid-size: 4 1;
            grid-gutter: 5;
            height: 15%;
            align: center top;
            padding: 0 0 0 0;
            border: none;
        }
    """

    def compose(self) -> ComposeResult:
        # yield Horizontal(
        #     Block(label="cpu", id="cpu"),
        #     Block(label="mem"),
        #     Block(label="disk"),
        #     Block(label="active user"),
        #     id="horitonzal_container"
        # )
        yield Block(label="cpu", id="cpu")
        yield Block(label="mem")
        yield Block(label="disk")
        yield Block(label="active user")
