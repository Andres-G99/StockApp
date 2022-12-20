#from GUI.add_prod_window import *
from tkinter import *
from tkinter import ttk
from BBDD.connect_bbdd import *


def add_item(codigo, nombre, cantidad, precio_unit, porcent_ag):
    precio_final = float(precio_unit + (precio_unit * (porcent_ag/100)))
    insertar_articulo(codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final)

'''
def crear_tabla(frame):
    datos = get_datos()
    param = ["Codigo", "Nombre", "Cantidad", "Precio unitario", "% Agregado", "Precio final"]
    for k in range(6):
        if param[k] == "Codigo":
            #self.e = Entry(frame, width=20)
            e = Text(frame, width=15, height=1)
            e.grid(row= 0, column= k)
            e.insert(END, param[k])
            e.config(state=DISABLED)
        elif param[k] == "Nombre":
            #self.e = Entry(frame, width=50)
            e = Text(frame, width=30, height=1)
            e.grid(row= 0, column= k)
            e.insert(END, param[k])
            e.config(state=DISABLED)
        else:
            #self.e = Entry(frame, width=30)
            e = Text(frame, width=20, height=1)
            e.grid(row= 0, column= k)
            e.insert(END, param[k])
            e.config(state=DISABLED)   

    for i in range(1,len(datos)):
        for j in range(6):
            if param[j] == "Codigo":
                e = Text(frame, width=15, height=1)
                e.grid(row=i, column= j)
                e.insert(END, datos[i][j])
                
            elif param[j] == "Nombre":
                e = Text(frame, width=30, height=1)
                e.grid(row=i, column= j)
                #e.insert(END, datos[i])
                e.insert(END, datos[i][j])
            else:
                e = Text(frame, width=20, height=1)
                e.grid(row=i, column= j)
                #e.insert(END, datos[i])
                e.insert(END, datos[i][j])
'''

def crear_tabla(frame):
    tabla = ttk.Treeview(frame)
    tabla['columns'] = ("Codigo", "Nombre", "Cantidad", "Precio unitario", "% Agregado", "Precio final")

    tabla.column("#0", anchor = W, width=30, minwidth= 25)
    tabla.column("Nombre", width=120, minwidth= 25)
    tabla.column("Cantidad", width=15, minwidth= 10)
    tabla.column("Precio unitario", width=15, minwidth= 10)
    tabla.column("% Agregado", width=15, minwidth= 10)  
    tabla.column("Precio final", width=15, minwidth= 10)

    tabla.heading("#0", text="Código", anchor = W)
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Precio unitario", text="Precio unitario")
    tabla.heading("% Agregado", text="% Agregado")
    tabla.heading("Precio final", text="Precio final")

    tabla.insert(parent='', index='end', text= "Padre", values=("ee648", "Mauina del mal", 2,4,5,6))

    tabla.pack()