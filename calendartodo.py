from textual.reactive import reactive
from textual.widgets import Static, Digits
from datetime import date, datetime

class CalendarTodo(Static):
    year = reactive("2024")
    month = reactive("3")
    day = reactive("25")
    t = reactive("0")
    currentTime = reactive(datetime.now().strftime("%H:%M:%S"))

    def on_mount(self):
        today = date.today()
        now = datetime.now()
        self.year = str(today.year)
        self.month = str(today.month)
        self.day = str(today)
        self.set_interval(1, self.update_time)

    def compose(self):
        yield Digits(self.currentTime, id="clock")

    def update_time(self):
        self.currentTime = datetime.now().strftime("%H:%M:%S")

    def watch_currentTime(self):
        try:
            self.query_one("#clock").update(self.currentTime)
        except Exception as e:
            pass
        # print("watch")
