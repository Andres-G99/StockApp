#from GUI.add_prod_window import *
from tkinter import *
from tkinter import ttk
from BBDD.connect_bbdd import *


def add_item(codigo, nombre, cantidad, precio_unit, porcent_ag):
    precio_final = float(precio_unit + (precio_unit * (porcent_ag/100)))
    insertar_articulo(codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final)
    dato = (codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final)
    add_record(dato)

def update_record(id, code, name, cantidad, prec_u, porc_ag):
    precio_final = float(prec_u + (prec_u * (porc_ag/100)))
    modificar_articulo(id, code, name, cantidad, prec_u, porc_ag, precio_final)
    destruir_tabla()

def crear_tabla(frame):
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
        tabla.insert(parent='', index='end', id= count, values=(None, dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]), tag = "par")
    else:
        tabla.insert(parent='', index='end', id= count, values=(None, dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]), tag = "impar")
    count += 1
    update_data()


def remove_record():
    del_item = tabla.selection()[0]
    dato = datos[int(del_item)]
    code = dato[0]
    eliminar_articulo(code)
    tabla.delete(del_item)
    destruir_tabla()

    
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
    destruir_tabla()

def decrement_record():
    selected = tabla.focus()
    values = tabla.item(selected, 'values')
    print(values[3])
    
    if (int(values[3]) - 1) <= 0:
        messagebox.showinfo("Error", "No hay mas unidades de este artículo")
        
    else:
        cantidad = (int(values[3]) - 1)
        modificar_unidad(values[0], cantidad)
        destruir_tabla()
    # if ((int(values[3]) - 1) == 0) or (values[3] == 0):
    #     messagebox.showinfo("Error", "No hay mas unidades de este artículo")
    # else:
    #     cantidad = int(values[3]) - 1
    #     modificar_unidad(values[0], cantidad)
    #     destruir_tabla()



def destruir_tabla():
    tabla.destroy()
    sb.destroy()