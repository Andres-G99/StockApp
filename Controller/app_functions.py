#from GUI.add_prod_window import *
from tkinter import *
from tkinter import ttk
from customtkinter import CTkScrollbar
import re

from BBDD.connect_bbdd import *


def add_item(codigo, nombre, cantidad, cantidad_min, precio_unit, porcent_ag):
    precio_final = float(precio_unit + (precio_unit * (porcent_ag/100)))
    insertar_articulo(codigo, nombre, int(cantidad), float(precio_unit), float(porcent_ag), precio_final, int(cantidad_min))
    dato = (codigo, nombre, int(cantidad), float(precio_unit), float(porcent_ag), precio_final, int(cantidad_min))
    add_record(dato)

def update_record(id, code, name, cantidad, cantidad_min, prec_u, porc_ag):
    precio_final = float(prec_u) + (float(prec_u) * (float(porc_ag)/100))
    modificar_articulo(id, code, name, cantidad, cantidad_min, prec_u, porc_ag, precio_final)
    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    tabla.item(selected, values=(id, code, name, cantidad, prec_u, porc_ag, precio_final, cantidad_min))

    #destruir_tabla()

def crear_tabla(frame, filtro, data):
    global tabla
    global sb
    #Scroll
    sb = CTkScrollbar(frame)
    sb.pack(side=RIGHT, fill=Y, padx=2, pady=5)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) 
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

    # tabla = ttk.Treeview(frame, height=160, yscrollcommand=sb.set, style="mystyle.Treeview")
    tabla = ttk.Treeview(frame, height=160, yscrollcommand=sb.set, style="mystyle.Treeview")
    tabla.pack(padx=5, pady=5)

    sb.configure(command=tabla.yview)
    tabla['columns'] = ("Id", "Codigo", "Nombre", "Cantidad", "Precio unitario", "% Agregado", "Precio final", "Cant min")


    tabla.column("#0", stretch = NO, width=0)
    tabla.column("Id", stretch = NO, width=0)
    tabla.column("Codigo", width=250, minwidth= 180)
    tabla.column("Nombre", width=400, minwidth= 340)
    tabla.column("Cantidad", width=200, minwidth= 180)
    tabla.column("Precio unitario", width=200, minwidth= 180)
    tabla.column("% Agregado", width=200, minwidth= 180)  
    tabla.column("Precio final", width=200, minwidth= 180)
    tabla.column("Cant min", stretch = NO, width=0)

    tabla.heading("#0", text="")
    tabla.heading("Id", text="Id")
    tabla.heading("Codigo", text="Código")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Precio unitario", text="Precio unitario")
    tabla.heading("% Agregado", text="% Agregado")
    tabla.heading("Precio final", text="Precio final")
    tabla.heading("Cant min", text='')
    
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
            tabla.insert(parent='', index='end', id= count, values=(datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], datos[i][6], datos[i][7]), tag = "par")
        else:
            tabla.insert(parent='', index='end', id= count, values=(datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], datos[i][6], datos[i][7]), tag = "impar")
        count += 1

    

def add_record(dato):
    global count
    if count % 2 == 0:
        tabla.insert(parent='', index='end', id= count, values=(count, dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6]), tag = "par")
    else:
        tabla.insert(parent='', index='end', id= count, values=(count, dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6]), tag = "impar")
    count += 1
    #print(dato)
    update_data()
    destruir_tabla()


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
    #print(values)
    return values

def increment_record():
    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    cantidad = int(values[3]) + 1
    modificar_unidad(values[0], cantidad, "inc")
    tabla.item(selected, values=(values[0], values[1], values[2], cantidad, values[4], values[5], values[6], values[7]))

def decrement_record():
    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    
    if (int(values[3]) - 1) < 0:
        messagebox.showinfo("Error", "No hay mas unidades de este artículo")
    else:
        cantidad = (int(values[3]) - 1)
        id = values[0]
        modificar_unidad(id, cantidad, "dec")
        tabla.item(selected, values=(values[0], values[1], values[2], cantidad, values[4], values[5], values[6], values[7]))

def destruir_tabla():
    tabla.destroy()
    sb.destroy()

def buscar(parametro, opcion):
    datos = []
    bbdata = get_datos()
    if opcion == "Por código":
        for dato in bbdata:
            if re.search(parametro, dato[1], re.IGNORECASE):
                datos.append(dato)
        destruir_tabla()
        return datos

    elif opcion == "Por nombre":
        for dato in bbdata:
            if re.search(parametro, dato[2], re.IGNORECASE):
                datos.append(dato)
        destruir_tabla()
        return datos       
    
    elif opcion == "Todos":
        for dato in bbdata:
            if re.search(parametro, dato[1], re.IGNORECASE) or re.search(parametro, dato[2], re.IGNORECASE):
                datos.append(dato)
        destruir_tabla()
        return datos

def ordenar_por_salida(): #odena por salida
    datos = get_datos()
    n = len(datos)
    for i in range(n-1):
        for j in range(n-1-i):
            if datos[j][9] < datos[j+1][9]:
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos
    #print(datos)

def ordenar_por_faltantes():
    datos = get_datos()
    n = len(datos)
    for i in range(n-1):
        for j in range(n-1-i):
            if (datos[j][7] - datos[j][3]) < (datos[j+1][7] - datos[j+1][3]):
                datos[j], datos[j+1] = datos[j+1], datos[j]
            if(datos[j+1][3] == 0):
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos

# def ordenar_por_faltantes():
#     datos = get_datos()
#     n = len(datos)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if (datos[j][3] <  datos[j+1][3]):
#                 datos[j], datos[j+1] = datos[j+1], datos[j]
#     return datos