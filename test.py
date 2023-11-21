from datetime import datetime
import PySimpleGUI as sg

def keritav(start_hour=None, start_minute=None, start_second=None):
    aken2 = {
        "font": ("Courier New", 48, "bold"),
        "enable_events": True,
        "background_color": None,
        "text_color": "white",
        "justification": "center",
        "pad": (0, 0)
    }
    hetkel = datetime.now()
    tund, minut, sekund = hetkel.hour, hetkel.minute, hetkel.second
    tund = tund if start_hour is None else max(0, min(int(start_hour), 23))
    minut = minut if start_minute is None else max(0, min(int(start_minute), 59))
    sekund = sekund if start_second is None else max(0, min(int(start_second), 59))
    aken1 = [
        [sg.Text(f"{tund:0>2d}", **aken2, size=(3, 1), key="Tund"),
         sg.Text(":",  **aken2),
         sg.Text(f"{minut:0>2d}", **aken2, size=(3, 1), key="Minut"),
         sg.Text(":",  **aken2),
         sg.Text(f"{sekund:0>2d}", **aken2, size=(3, 1), key="Sekund")],
        [sg.Button("OK"), sg.Button("Cancel")],
    ]
    window = sg.Window("Vali aeg", aken1, grab_anywhere=True, keep_on_top=True, modal=True, finalize=True)
    tund_element, minut_element, sekund_element = window['Tund'], window['Minut'], window['Sekund']
    tund_element.bind("<MouseWheel>", "_Wheel")
    minut_element.bind("<MouseWheel>", "_Wheel")
    sekund_element.bind("<MouseWheel>", "_Wheel")
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            window.close()
            return (None, None, None)
        elif event == "OK":
            window.close()
            return (tund, minut, sekund)
        elif event == "Tund_Wheel":
            delta = -int(tund_element.user_bind_event.delta/120)
            tund = (tund+delta) % 24
            tund_element.update(f'{tund:0>2d}')
        elif event == "Minut_Wheel":
            delta = -int(minut_element.user_bind_event.delta/120)
            minut = (minut+delta) % 60
            minut_element.update(f'{minut:0>2d}')
        elif event == "Sekund_Wheel":
            delta = -int(sekund_element.user_bind_event.delta/120)
            sekund = (sekund+delta) % 60
            sekund_element.update(f'{sekund:0>2d}')
sg.theme("DarkBlue")

layout = [[sg.Button('Õppima')],]
window1 = sg.Window('Title', layout, finalize=True)
while True:
    event, values = window1.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Õppima':
        window1.close()
        tund, minut, sekund = keritav(5, 20, 10)
        print(f'Määrasid ajaks {tund:0>2d}:{minut:0>2d}:{sekund:0>2d}')

