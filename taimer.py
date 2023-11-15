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
ttk.Label(frame, text="Sisesta õppimisperioodi pikkus(eeldame, et sisestatakse (muidu ei tööta) minutid ja sekundid kujul --> mm:ss):").grid(row=0)
ttk.Label(frame, text="Sisesta puhkusperioodi pikkus(eeldame, et sisestatakse (muidu ei tööta) minutid ja sekundid kujul --> mm:ss):").grid(row=1)


õpi_aeg = ttk.Entry(frame) # õpi ja puhkus_aeg on kasutaja poolt määratud ajaperioodid
puhkus_aeg = ttk.Entry(frame)

õpi_aeg.grid(row=0, column=1)
puhkus_aeg.grid(row=1, column=1)


#Kui aeg parajasti ei jookse, siis vajutades nuppu start jooksutatakse kas õppimise_aja_määramine() või puhkamise_aja_määramine() (kordamööda)
def õppimise_aja_määramine():
    a, b = õpi_aeg.get().split(":")
    aeg.set(f"{a}:{b}")

def puhkamise_aja_määramine():
    a, b = puhkus_aeg.get().split(":")
    aeg.set(f"{a}:{b}")

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
