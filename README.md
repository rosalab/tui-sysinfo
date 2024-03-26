# TUI Sysinfo

TuiSysInfo is a terminal-based system information application developed in Python. It uses the Textual library to create a rich, interactive user interface in the terminal. The application displays system information, current time in different time zones, and weather information.

## Features
- System Information: Displays system information such as CPU usage, memory usage, disk usage, and the active user.
- Clocks: Displays the current time in different time zones including America/New_York, UTC, and Etc/GMT+12.
- Weather: Fetches and displays the current weather information

## Installation

```
git clone git@github.com:w93163red/tui-sysinfo.git
cd tui-sysinfo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
textual run App.py
```

## Directories / Files
- App.py: The main application script that runs the TuiSysInfo application.
- View/: contains the component that constructs the page
- Widgets/: Contains the custom widgets that build the component

## Screenshot

![image](https://github.com/w93163red/tui-sysinfo/assets/7308728/f05aa802-743b-4a1f-8421-2b058404fe1a)
