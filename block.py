from textual import events
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static, Digits
from textual.containers import Container
import psutil

class Block(Static, inherit_bindings=False):
    DEFAULT_CSS = """
        Block {
            align-horizontal: center;
            layout: grid;
            grid-size: 1 2;
            border: dashed red;
            width: 15%;
            margin-right: 5;
        }

        .title {
            height: 1fr;
            width: 1fr;
            padding: 0;
            margin: 0;
        }
        
        .digits {
            width: 1fr;
            height: 1fr;
        }
    """

    text = reactive("0.0", recompose=True)

    def __init__(self, label,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)

        self.label = label
        self.func_maps = {
            'cpu': {'title': 'CPU USAGE', 'updateFunc': self.update_cpu},
            'mem': {'title': 'MEM USAGE', 'updateFunc': self.update_mem},
            'disk': {'title': 'DISK USAGE', 'updateFunc': self.update_disk},
            'active user': {'title': 'Active Sessions', 'updateFunc': self.update_active_sessions},
        }

    def on_mount(self):
        self.set_interval(1, self.func_maps[self.label]['updateFunc'])

    def update_cpu(self):
        self.text = str(psutil.cpu_percent()) + "%"

    def update_mem(self):
        self.text = str(psutil.virtual_memory().percent) + "%"

    def update_disk(self):
        self.text = str(psutil.disk_usage('/').percent) + "%"

    def update_active_sessions(self):
        self.text = str(psutil.users())

    def compose(self) -> ComposeResult:
        yield Static(self.func_maps[self.label]['title'], classes="title")
        yield Digits(self.text, classes="digits")
