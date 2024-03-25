from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal
from block import Block

class Sysinfo(Static):
    CSS_PATH = "tcss/sysinfo.tcss"
    
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Block("TWO", classes="inner-box"),
            Static("Two", classes="inner-box"),
            Static("three", classes="inner-box"),
            Static("four", classes="inner-box"),
        )
        