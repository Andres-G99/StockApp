#from GUI.add_prod_window import *
from tkinter import *
from tkinter import ttk
from BBDD.connect_bbdd import *


def add_item(codigo, nombre, cantidad, precio_unit, porcent_ag):
    precio_final = float(precio_unit + (precio_unit * (porcent_ag/100)))
    insertar_articulo(codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final)
    dato = (codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final)
    add_record(dato)



def crear_tabla(frame):
    global tabla
    tabla = ttk.Treeview(frame, height=150)
    tabla['columns'] = ("Codigo", "Nombre", "Cantidad", "Precio unitario", "% Agregado", "Precio final")


    tabla.column("#0", width=1, stretch = NO)
    tabla.column("Codigo", width=200, minwidth= 190)
    tabla.column("Nombre", width=300, minwidth= 290)
    tabla.column("Cantidad", width=170, minwidth= 160)
    tabla.column("Precio unitario", width=170, minwidth= 160)
    tabla.column("% Agregado", width=170, minwidth= 160)  
    tabla.column("Precio final", width=170, minwidth= 160)

    tabla.heading("#0", text="")
    tabla.heading("Codigo", text="Código")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Precio unitario", text="Precio unitario")
    tabla.heading("% Agregado", text="% Agregado")
    tabla.heading("Precio final", text="Precio final")

    #tabla.insert(parent='', index='end', values=("ee648", "Maquina del mal", 2,4,5,6))
    
    global count, datos
    datos = get_datos()
    count = 0

    for i in range(len(datos)):
        tabla.insert(parent='', index='end', id= count, values=(datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], datos[i][6]))
        count += 1

    tabla.pack(padx=0)

def add_record(dato):
    global count
    tabla.insert(parent='', index='end', id= count, values=(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]))
    count += 1

def remove_record():
    del_item = tabla.selection()[0]
    dato = datos[int(del_item)]
    code = dato[0]
    eliminar_articulo(code)
    tabla.delete(del_item)
    





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