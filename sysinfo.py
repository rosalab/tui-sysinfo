from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static
from block import Block

class Sysinfo(Static):
    DEFAULT_CSS = """
        Sysinfo {
            height: 25%;
            align: center top;
        }
    """
    
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Block(label="cpu"),
            Block(label="mem"),
            Block(label="disk"),
            Block(label="active user"),
        )
        # yield Block()
        # yield Block()
        # yield Block()
        # yield Block()
