from algortimo import ruta_a_seguir
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from dataBaseConections import getAllPlaces, updateAPI, getCoordinates
from time import sleep

app = tk.Tk()
app.title("Rutas La Asunción")

places = getAllPlaces()
combs = [ttk.Combobox(app, values = places) for i in range(3)]



def add_combox():
    combs.append(ttk.Combobox(app, values = places))
    combs[-1].grid(column = 20, row = 20 + ( (i + len(combs)) * 10))

def calcular ():
    l = []
    for i in combs:
        if(i.get()):
            a = i.get()
            l.append(a)

    if(len(l) <= 1):
        mensajes.config(text = "\nERROR: Solo hay " + str(len(l)) + " ubicaciones registadas")
        return
    else:
        mensajes.config(text = "\nCalculando ...")
        sleep(0.2)

    lcc = {}

    for i in l:
        lcc[i] = getCoordinates(i)
    ruta = ruta_a_seguir(lcc)

    mensajes.config(text = "\nLa ruta a seguir es:\n"+ruta[0]+"\n Se espera un tiempo de: " + str(ruta[1]/60) + " minutos (Sin considerar tiempos de descarga)")

def changeAPI ():
    app2 = tk.Tk()
    def callback():
        if(en.get()):
            st = en.get()
            det = updateAPI(st)
            messagebox.showinfo("Éxito","La clave API ha sido cambiada!")
            app2.destroy()
        else:
            messagebox.showerror("Error","Favor de revisar la clave ingresada")
        
    p1 = tk.Label(app2,text = "Ingrese la nueva clave API").grid(column = 0 ,row = 0)

    en = tk.Entry(app2, width = 7)
    en.grid(column = 0 ,row = 1)

    bot1 = tk.Button(app2, text = "Cambiar clave", command = callback).grid(column = 0 ,row = 2)


app.geometry(("1500x840"))


titulo = tk.Label(app,text = "\tIngrese las ubicaciones",font = ('Helvetica', 30, 'bold'))
titulo.grid(row = 10, column = 10, columnspan = 20 )


for i in range(len(combs)):
    combs[i].grid(column = 20, row = 20 + (i * 10))

space1 = tk.Label(app,text=" ").grid(column = 1000, row = 999)

add = tk.Button(app, text = " Agregar Ubicacion ", command = add_combox)
add.grid(column = 10, row = 1000 )

cal = tk.Button(app, text = " Calcular ruta ", command = calcular )
cal.grid(column = 20, row = 1000 )

api = tk.Button(app, text = " Cambiar clave API ", command = changeAPI)
api.grid(column = 30, row = 1000 )


mensajes = tk.Label(app, text = " "  )
mensajes.grid(row = 500, column = 20)

def on_closing():
    if messagebox.askokcancel("Cerrar", "¿Seguro que desas salir?"):
        app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()
