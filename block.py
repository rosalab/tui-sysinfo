from textual import events
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Static, Digits
import psutil

class Block(Static, inherit_bindings=False):
    DEFAULT_CSS = """
        Block {
            align-horizontal: center;
            box-sizing: content-box;
            border: round white;
            width: 100%;
            border-title-style: italic;
            border-title-align: center;
        }
      
        .digits {
            padding: 1;
            text-align: center;
        }
    """

    text = reactive("0.0")

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
        self.border_title = self.func_maps[self.label]['title']
        self.set_interval(1, self.func_maps[self.label]['updateFunc'])

    def watch_text(self):
        try:
            self.query_one(Digits).update(self.text)
        except Exception as e:
            pass

    def update_cpu(self):
        self.text = str(psutil.cpu_percent()) + "%"

    def update_mem(self):
        self.text = str(psutil.virtual_memory().percent) + "%"

    def update_disk(self):
        self.text = str(psutil.disk_usage('/').percent) + "%"

    def update_active_sessions(self):
        self.text = str(len(psutil.users()))

    def compose(self) -> ComposeResult:
        yield Digits(self.text, classes="digits")
