from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import *
from datetime import datetime

def keritav(start_hour=None, start_minute=None, start_second=None):
    def on_wheel(event, element):
        nonlocal tund, minut, sekund
        delta = -int(event.delta / 120)
        if element == "Tund":
            tund = (tund + delta) % 24
        elif element == "Minut":
            minut = (minut + delta) % 60
        elif element == "Sekund":
            sekund = (sekund + delta) % 60
        update_time()
    def on_wheel1(event, element):
        nonlocal tund1, minut1, sekund1
        delta = -int(event.delta / 120)
        if element == "Tund1":
            tund1 = (tund1 + delta) % 24
        elif element == "Minut1":
            minut1 = (minut1 + delta) % 60
        elif element == "Sekund1":
            sekund1 = (sekund1 + delta) % 60
        update_time1()

    def update_time():
        nonlocal tund, minut, sekund
        tund_label.config(text=f"{tund:0>2d}")
        minut_label.config(text=f"{minut:0>2d}")
        sekund_label.config(text=f"{sekund:0>2d}")
    def update_time1():
        nonlocal tund, minut, sekund
        tund1_label.config(text=f"{tund1:0>2d}")
        minut1_label.config(text=f"{minut1:0>2d}")
        sekund1_label.config(text=f"{sekund1:0>2d}")

    def on_ok():
        global valik_aeg
        global valik_aeg1
        nonlocal tund, minut, sekund
        valik_aeg = f"{tund:0>2d}:{minut:0>2d}:{sekund:0>2d}"
        valik_aeg1 = f"{tund1:0>2d}:{minut1:0>2d}:{sekund1:0>2d}"
        window.destroy()
    tund, minut, sekund = 0, 0, 0 
    tund1, minut1, sekund1 = 0, 0, 0
    window = Tk()
    frame = ttk.Frame(window, padding=10)
    frame.pack()

    window.geometry("800x600")
    
    tund = tund if start_hour is None else max(0, min(int(start_hour), 23))
    minut = minut if start_minute is None else max(0, min(int(start_minute), 59))
    sekund = sekund if start_second is None else max(0, min(int(start_second), 59))
   
    
    tund1_label = Label(window, font=("Courier New", 48, "bold"))
    minut1_label = Label(window, font=("Courier New", 48, "bold"))
    sekund1_label = Label(window, font=("Courier New", 48, "bold"))

    tund_label = Label(window, font=("Courier New", 48, "bold"))
    minut_label = Label(window, font=("Courier New", 48, "bold"))
    sekund_label = Label(window, font=("Courier New", 48, "bold"))

    tund_label.place(relx=.3, rely=.3, anchor="center")
    Label(window, text=":", font=("Courier New", 48, "bold")).place(relx=.4, rely=.3, anchor="center")
    minut_label.place(relx=.5, rely=.3, anchor="center")
    Label(window, text=":", font=("Courier New", 48, "bold")).place(relx=.6, rely=.3, anchor="center")
    sekund_label.place(relx=.7, rely=.3, anchor="center")
    
    Label(window, text="Õppimise aeg", font=("Courier New", 20, "bold")).place(relx=.5, rely=.2, anchor="center")
    Label(window, text="Puhkamise aeg", font=("Courier New", 20, "bold")).place(relx=.5, rely=.4, anchor="center")
    
    tund1_label.place(relx=.3, rely=.5, anchor="center")
    Label(window, text=":", font=("Courier New", 48, "bold")).place(relx=.4, rely=.5, anchor="center")
    minut1_label.place(relx=.5, rely=.5, anchor="center")
    Label(window, text=":", font=("Courier New", 48, "bold")).place(relx=.6, rely=.5, anchor="center")
    sekund1_label.place(relx=.7, rely=.5, anchor="center")
    
    tund_label.config(text=f"{tund:0>2d}")
    minut_label.config(text=f"{minut:0>2d}")
    sekund_label.config(text=f"{sekund:0>2d}")
    
    tund1_label.config(text=f"{tund1:0>2d}")
    minut1_label.config(text=f"{minut1:0>2d}")
    sekund1_label.config(text=f"{sekund1:0>2d}")
    
    tund1_label.bind("<MouseWheel>", lambda event: on_wheel1(event, "Tund1"))
    minut1_label.bind("<MouseWheel>", lambda event: on_wheel1(event, "Minut1"))
    sekund1_label.bind("<MouseWheel>", lambda event: on_wheel1(event, "Sekund1"))

    tund_label.bind("<MouseWheel>", lambda event: on_wheel(event, "Tund"))
    minut_label.bind("<MouseWheel>", lambda event: on_wheel(event, "Minut"))
    sekund_label.bind("<MouseWheel>", lambda event: on_wheel(event, "Sekund"))
    

    ok_button = ttk.Button(window, text="OK", command=on_ok)
    ok_button.place(relx=.5, rely=.7, anchor="center")

    window.mainloop()

    
    

keritav()
õppimine = valik_aeg
puhkamine = valik_aeg1
print(õppimine)
print(puhkamine)

window = Tk()
frame = ttk.Frame(window, padding=10)
frame.pack()
frame.place()
window.geometry("800x600")

aeg = StringVar()
aeg.set(õppimine)
taimer = tk.Label(window, textvariable=aeg, font=("consolas", 60))
taimer.place(relx=.5, rely=.5, anchor="center")


#Kui aeg parajasti ei jookse, siis vajutades nuppu start jooksutatakse kas õppimise_aja_määramine() või puhkamise_aja_määramine() (kordamööda)
def õppimise_aja_määramine():
    a, b, c = õppimine.split(":")
    aeg.set(f"{a}:{b}:{c}")

def puhkamise_aja_määramine():
    a, b, c = puhkamine.split(":")
    aeg.set(f"{a}:{b}:{c}")

# muutus_ajas funktsioon kutusb iseennast esile, kuni taimer jookseb 00:00-ni. Kui kasutaja vajutab paus, siis 
def muutus_ajas():
    global paus, töötamine, aeg_jookseb
    if paus == False:
        ühikud = list(map(int, aeg.get().split(":")))
        sekundid = sum((x*(60**i) for i, x in enumerate(reversed(ühikud))))

        
    

        if sekundid > 0:
            sekundid -= 1
            tunnid = sekundid // 3600
            minutid = sekundid // 60
            sekundid = sekundid % 60

            #kui mõni null on puudu, lisatakse see sõne ette. Nt jäänud on 5 sekundit -> "05"
            tunnid, minutid, sekundid = tuple(str(x) if x >= 10 else "0"+str(x) for x in [tunnid, minutid, sekundid])
            print(tunnid, minutid, sekundid)


            #kui tunnid on 0 siis kasutaja seda ei näe
            if tunnid == "00":
                aeg.set(f"{minutid}:{sekundid}")
            else:
                aeg.set(f"{tunnid}:{minutid}:{sekundid}")
            
            if sekundid == "00" and minutid == "00" and tunnid == "00":
                taimer_punaseks()
                aeg_jookseb = False
                if töötamine == False:
                    töötamine = True
                else:
                    töötamine = False
            else:
                window.update()
                frame.after(1000, muutus_ajas)
    else:
        frame.after(10, muutus_ajas)

def paus_func():
    global paus
    paus = True

def start():
    print("Start")
    global paus, aeg_jookseb
    paus = False
    if aeg_jookseb == False:
        print("Aeg läheb käima")

        #taimeri värv mustaks
        taimer.config(fg="#000000")
        if töötamine == True:
            õppimise_aja_määramine()
        else:
            puhkamise_aja_määramine()
        muutus_ajas()

    aeg_jookseb = True
    


#värvimuutused
def taimer_punaseks():
    if aeg_jookseb == False:
        taimer.config(fg="#FF0000")
    window.update()
    frame.after(500, taimer_mustaks)
def taimer_mustaks():
    taimer.config(fg="#000000")
    window.update()
    if aeg_jookseb == False:
        frame.after(500, taimer_punaseks)


paus = True
töötamine = True #töötamine = True, kui käsil on õppimissessioon, töötamine = False, kui käsil on puhkepaus
aeg_jookseb = False #selleks, et start nuppu mitu korda vajutades ei panda aega alusest peale käima


start_nupp = ttk.Button(window, text="Start", command=start)
start_nupp.place(in_=taimer, relx=0.1, x=0, rely=1.0)

paus_nupp = ttk.Button(window, text="Paus", command=paus_func)
paus_nupp.place(in_=taimer, rely=1.0, relx=0.55)


window.mainloop()
