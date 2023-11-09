from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import *
window = Tk()
frame = ttk.Frame(window, padding=10)
frame.pack()
frame.place()
window.geometry("800x600")

aeg = StringVar()
aeg.set("00:10")
taimer = tk.Label(window, textvariable=aeg, font=("consolas", 60))
taimer.place(relx=.5, rely=.5, anchor="center")
ttk.Label(frame, text="Sisesta õppimisperioodi pikkus:").grid(row=0)
ttk.Label(frame, text="Sisesta puhkusperioodi pikkus:").grid(row=1)

õpi_aeg = ttk.Entry(frame)
puhkus_aeg = ttk.Entry(frame)

õpi_aeg.grid(row=0, column=1)
puhkus_aeg.grid(row=1, column=1)



def muutus_ajas():
    global paus
    if paus == False:
        ühikud = list(map(int, aeg.get().split(":")))
        sekundid = sum((x*(60**i) for i, x in enumerate(reversed(ühikud))))

        
    

        if sekundid > 0:
            sekundid -= 1
            tunnid = sekundid // 3600
            minutid = sekundid // 60
            sekundid = sekundid % 60

            tunnid, minutid, sekundid = tuple(str(x) if x >= 10 else "0"+str(x) for x in [tunnid, minutid, sekundid])
            print(tunnid, minutid, sekundid)


            #kui tunnid on 0 siis kasutaja seda ei näe
            if tunnid == "00":
                aeg.set(f"{minutid}:{sekundid}")
            else:
                aeg.set(f"{tunnid}:{minutid}:{sekundid}")
            
            if sekundid == "00" and minutid == "00" and tunnid == "00":
                taimer_punaseks()
            else:
                window.update()
                frame.after(1000, muutus_ajas)
    else:
        frame.after(10, muutus_ajas)

def paus_func():
    global paus
    paus = True
def start():
    global paus
    paus = False


#värvimuutused
def taimer_punaseks():
    taimer.config(fg="#FF0000")
    window.update()
    frame.after(500, taimer_mustaks)
def taimer_mustaks():
    taimer.config(fg="#000000")
    window.update()
    frame.after(500, taimer_punaseks)


paus = True
muutus_ajas()
start_nupp = ttk.Button(window, text="Start", command=start)
start_nupp.place(in_=taimer, relx=0.1, x=0, rely=1.0)

paus_nupp = ttk.Button(window, text="Paus", command=paus_func)
paus_nupp.place(in_=taimer, rely=1.0, relx=0.55)

window.mainloop()