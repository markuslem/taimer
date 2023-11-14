from datetime import datetime
import PySimpleGUI as sg

def popup_get_time(start_hour=None, start_minute=None):
    """
    Using mouse wheel to select hour and minute
    :param start_hour: Default value for hour. 0 ~ 23
    :type start_hour: int
    :param start_minute: Default value for hour. 0 ~ 59
    :type start_minute: int
    """
    option = {
        "font": ("Courier New", 48, "bold"),
        "enable_events": True,
        "background_color": None,
        "text_color": "white",
        "justification": "center",
        "pad": (0, 0)
    }
    now = datetime.now()
    hour, minute = now.hour, now.minute
    hour = hour if start_hour is None else max(0, min(int(start_hour), 23))
    minute = minute if start_minute is None else max(0, min(int(start_minute), 59))
    layout = [
        [sg.Text(f"{hour:0>2d}", **option, size=(3, 1), key="Hour"),
         sg.Text(":",  **option),
         sg.Text(f"{minute:0>2d}", **option, size=(3, 1), key="Minute")],
        [sg.Button("OK"), sg.Button("Cancel")],
    ]
    window = sg.Window("Select Time", layout, grab_anywhere=True,
        keep_on_top=True, modal=True, finalize=True)
    hour_element, minute_element = window['Hour'], window['Minute']
    hour_element.bind("<MouseWheel>", "_Wheel")
    minute_element.bind("<MouseWheel>", "_Wheel")

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            window.close()
            return (None, None)
        elif event == "OK":
            window.close()
            return (hour, minute)
        elif event == "Hour_Wheel":
            delta = -int(hour_element.user_bind_event.delta/120)
            hour = (hour+delta) % 24
            hour_element.update(f'{hour:0>2d}')
        elif event == "Minute_Wheel":
            delta = -int(minute_element.user_bind_event.delta/120)
            minute = (minute+delta) % 60
            minute_element.update(f'{minute:0>2d}')

sg.theme("DarkBlue")

layout = [
    [sg.Button('Date')],
]
window = sg.Window('Title', layout, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Date':
        hour, minute = popup_get_time(5, 20)
        print(f'You set time as {hour:0>2d}:{minute:0>2d}')

window.close()