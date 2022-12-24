#from GUI.add_prod_window import *
from tkinter import *
from tkinter import ttk
import re

from BBDD.connect_bbdd import *


def add_item(codigo, nombre, cantidad, precio_unit, porcent_ag):
    precio_final = float(precio_unit + (precio_unit * (porcent_ag/100)))
    insertar_articulo(codigo, nombre, int(cantidad), float(precio_unit), float(porcent_ag), precio_final)
    dato = (codigo, nombre, int(cantidad), float(precio_unit), float(porcent_ag), precio_final)
    add_record(dato)

def update_record(id, code, name, cantidad, prec_u, porc_ag):
    precio_final = float(prec_u + (prec_u * (porc_ag/100)))
    modificar_articulo(id, code, name, cantidad, prec_u, porc_ag, precio_final)
    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    tabla.item(selected, values=(id, code, name, cantidad, prec_u, porc_ag, precio_final))

    #destruir_tabla()

def crear_tabla(frame, filtro, data):
    global tabla
    global sb
    #Scroll
    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=Y)

    tabla = ttk.Treeview(frame, height=150, yscrollcommand=sb.set)
    tabla.pack(padx=0)

    sb.config(command=tabla.yview)
    tabla['columns'] = ("Id", "Codigo", "Nombre", "Cantidad", "Precio unitario", "% Agregado", "Precio final")


    tabla.column("#0", stretch = NO, width=1)
    tabla.column("Id", stretch = NO, width=1)
    tabla.column("Codigo", width=200, minwidth= 190)
    tabla.column("Nombre", width=300, minwidth= 290)
    tabla.column("Cantidad", width=170, minwidth= 160)
    tabla.column("Precio unitario", width=170, minwidth= 160)
    tabla.column("% Agregado", width=170, minwidth= 160)  
    tabla.column("Precio final", width=170, minwidth= 160)

    tabla.heading("#0", text="")
    tabla.heading("Id", text="Id")
    tabla.heading("Codigo", text="Código")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Precio unitario", text="Precio unitario")
    tabla.heading("% Agregado", text="% Agregado")
    tabla.heading("Precio final", text="Precio final")

    
    global count, datos
    if filtro == True:
        datos = data
    else:
        datos = get_datos()
    count = 0

    tabla.tag_configure('impar', background = "white")
    tabla.tag_configure('par', background = "lightblue")

    for i in range(len(datos)):
        if count % 2 == 0:
            tabla.insert(parent='', index='end', id= count, values=(datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], datos[i][6]), tag = "par")
        else:
            tabla.insert(parent='', index='end', id= count, values=(datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], datos[i][6]), tag = "impar")
        count += 1

    

def add_record(dato):
    global count
    if count % 2 == 0:
        tabla.insert(parent='', index='end', id= count, values=(count, dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]), tag = "par")
    else:
        tabla.insert(parent='', index='end', id= count, values=(count, dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]), tag = "impar")
    count += 1
    update_data()


def remove_record():
    del_item = tabla.selection()[0]
    dato = datos[int(del_item)]
    code = dato[0]
    eliminar_articulo(code)
    tabla.delete(del_item)
    destruir_tabla() #para que la lineas queden intercaladas

    
def update_data():
    global datos
    datos = get_datos()


def selected_record():
    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    return values

def increment_record():
    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    cantidad = int(values[3]) + 1
    modificar_unidad(values[0], cantidad)
    tabla.item(selected, values=(values[0], values[1], values[2], cantidad, values[4], values[5], values[6]))

def decrement_record():
    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    
    if (int(values[3]) - 1) < 0:
        messagebox.showinfo("Error", "No hay mas unidades de este artículo")
    else:
        cantidad = (int(values[3]) - 1)
        id = values[0]
        modificar_unidad(id, cantidad)
        tabla.item(selected, values=(values[0], values[1], values[2], cantidad, values[4], values[5], values[6]))

def destruir_tabla():
    tabla.destroy()
    sb.destroy()

def buscar(parametro):
    datos = []
    bbdata = get_datos()
    for dato in bbdata:
        if re.search(parametro, dato[1], re.IGNORECASE):
            datos.append(dato)
    destruir_tabla()
    return datos

    