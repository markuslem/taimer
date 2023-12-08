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

    #õppeainete salvestamine
'''

    
    def värskenda_õppeaineid():
        
        with open("ained.txt", encoding="utf8") as f:
            faili_sisu = f.read()
            faili_sisu = faili_sisu.splitlines()
            global faili_pikkus
            faili_pikkus = len(faili_sisu)
            for i, aine in enumerate(faili_sisu):
                aine_label = Label(window, text=aine, font=("Courier New", 12))
                aine_label.grid(row=5+i, columnspan=5)
        
        global õppeaine_input, lisa_button
        õppeaine_input = tk.Entry(window)
        print(õppeaine_input)
        õppeaine_input.grid(row=3+faili_pikkus, column=0)

        lisa_button = Button(window, text="Lisa", command=lisa_faili)
        lisa_button.grid(row=3+faili_pikkus, column=1)
    
    def lisa_faili(): # eemaldatakse entry ja button widgetid ja lisatakse input faili.
        global õppeaine_input, lisa_button
        rida = õppeaine_input.get()
        õppeaine_input.destroy(); lisa_button.destroy()
        with open("ained.txt", "a" ,encoding="utf8") as f:
            print(rida)
            f.write("\n"+rida)
        värskenda_õppeaineid()
    värskenda_õppeaineid()

    
'''

    
    

keritav()
õppimine = valik_aeg
puhkamine = valik_aeg1
print(õppimine)
print(puhkamine)