#from GUI.add_prod_window import *
from tkinter import *
from BBDD.connect_bbdd import *


def add_item(codigo, nombre, cantidad, precio_unit, porcent_ag):
    print(codigo)
    print(precio_unit)
    print(porcent_ag)
    precio_final = float(precio_unit + (precio_unit * (porcent_ag/100)))
    insertar_articulo(codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final)

def crear_tabla(frame):
    #datos = get_datos()
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

    for i in range(1,30):
        for j in range(6):
            if param[j] == "Codigo":
                e = Text(frame, width=15, height=1)
                e.grid(row=i, column= j)
                #e.insert(END, datos[i])
            elif param[j] == "Nombre":
                e = Text(frame, width=30, height=1)
                e.grid(row=i, column= j)
                #e.insert(END, datos[i])
            else:
                e = Text(frame, width=20, height=1)
                e.grid(row=i, column= j)
                #e.insert(END, datos[i])


