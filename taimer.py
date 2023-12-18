from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkcalendar import *
import datetime
import pandas as pd

#aja_valimine.py
from aja_valimine import õppimine, puhkamine

window = Tk()
frame = ttk.Frame(window, padding=10)
frame.pack()
frame.place()
window.geometry("800x600")

#sakkide lisamine lehele
tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Taimer') 
tabControl.add(tab2, text ='Statistika') 
tabControl.pack(expand = 1, fill ="both") 

aeg = StringVar()
aeg.set(õppimine)
taimer = tk.Label(tab1, textvariable=aeg, font=("consolas", 60))
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
    global paus, töötamine, aeg_jookseb, sessiooni_aeg
    if paus == False:
        ühikud = list(map(int, aeg.get().split(":")))
        sekundid = sum((x*(60**i) for i, x in enumerate(reversed(ühikud))))

        
    

        if sekundid > 0:
            sekundid -= 1
            if töötamine == True: sessiooni_aeg += 1 #käib õppimise sessioon, mitte puhkus
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
                aeg_jookseb = False
                taimer_punaseks()
                uuenda_statistikat(sessiooni_aeg)
                sessiooni_aeg = 0
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
    global paus, sessiooni_aeg
    paus = True
    uuenda_statistikat(sessiooni_aeg)
    sessiooni_aeg = 0

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

def uuenda_statistikat(sessiooni_aeg):
    df = pd.read_csv("kulutatud_aeg.csv")
    df.loc[df['õppeaine'] == 'kokku', 'aeg'] += sessiooni_aeg # kokku aja uuendamine
    
    # vastava õppeaine aja uuendamine
    valitu = valitud_aine.get()
    if df['õppeaine'].isin([valitu]).any():
        df.loc[df['õppeaine'] == valitu, 'aeg'] += sessiooni_aeg
    #juhul kui õppeainet ei ole kulutatud_aeg.csv failis
    else:
        andmed = [{'õppeaine': valitu, 'aeg': sessiooni_aeg}]
        uus_rida = pd.DataFrame(andmed)
        df = df._append(uus_rida, ignore_index=True)
    
    df.to_csv("kulutatud_aeg.csv", index=False, columns=['õppeaine', 'aeg'])

    eemalda_statistika_lehekülg()
    uuenda_statistika_lehekülge()
    


paus = True
töötamine = True #töötamine = True, kui käsil on õppimissessioon, töötamine = False, kui käsil on puhkepaus
aeg_jookseb = False #selleks, et start nuppu mitu korda vajutades ei panda aega alusest peale käima

sessiooni_aeg = 0

start_nupp = ttk.Button(tab1, text="Start", command=start)
start_nupp.place(in_=taimer, relx=0.1, x=0, rely=1.0)

paus_nupp = ttk.Button(tab1, text="Paus", command=paus_func)
paus_nupp.place(in_=taimer, rely=1.0, relx=0.55)

with open('ained.txt', encoding='UTF-8') as f:
    sisu = f.readlines()
    sisu = [x.strip() for x in sisu]

    valitud_aine = StringVar()
    valitud_aine.set(sisu[0])

    nimekiri = OptionMenu(tab1, valitud_aine, *sisu)
    nimekiri.place(relx=0.5, rely=0.75)

def eemalda_statistika_lehekülg():
    global statistika_pealkiri, tree
    statistika_pealkiri.destroy()
    tree.destroy()


def uuenda_statistika_lehekülge():
    #statistika leht
    global statistika_pealkiri, tree
    statistika_pealkiri = ttk.Label(tab2, text="Statistika", font=("consolas", 60))
    statistika_pealkiri.pack()
    with open('kulutatud_aeg.csv', encoding='UTF-8') as f:
        sisu = [x.strip().split(",") for x in f.readlines()]
        
        tree = ttk.Treeview(tab2, column=("c1", "c2"), show='headings', height=len(sisu))
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Õppeaine")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Õpitud aeg")


        for õppeaine, kulunud_aeg in sisu[1:]:
            kulunud_aeg = int(float(kulunud_aeg))

            kulunud_aeg = str(datetime.timedelta(seconds=kulunud_aeg))

            
            print(õppeaine)
            tree.insert('', 'end', values=(õppeaine, kulunud_aeg))

        tree.pack()
uuenda_statistika_lehekülge()

window.mainloop()
uuenda_statistikat(sessiooni_aeg) #kui programm pannakse ilma pausimata kinni