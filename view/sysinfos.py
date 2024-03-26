from textual.app import ComposeResult
from textual.widgets import Static

from widgets.sysinfo import SysInfo


class SysInfos(Static):
    DEFAULT_CSS = """
        SysInfos {
            layout: grid;
            grid-size: 4 1;
            grid-gutter: 5;
            height: 10%;
            min-height: 7;
            align: center top;
            padding: 0 0 0 0;
            border: none;
            background: $primary-darken-1;
        }
    """

    def compose(self) -> ComposeResult:
        yield SysInfo(label="cpu", id="cpu")
        yield SysInfo(label="mem")
        yield SysInfo(label="disk")
        yield SysInfo(label="active user")
