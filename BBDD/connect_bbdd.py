import sqlite3
from tkinter import messagebox

def create_bbdd():
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    try:
        cursor.execute('''
        CREATE TABLE STOCKITEMS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CODIGO VARCHAR(20),
            NOMBRE VARCHAR(50),
            CANTIDAD INTEGER(10),
            PRECIO_UNIT FLOAT(15),
            PORCENT_AG FLOAT(10),
            PRECIO_FINAL FLOAT(15),
            CANTIDAD_MIN INTEGER(10),
            INGRESOS INTEGER(50),
            SALIDAS INTEGER(50))
        ''')
    except:
        messagebox.showwarning("Error BBDD", "La BBDD ya existe")


def insertar_articulo(codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final, cantidad_min):
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    primer_ingreso = cantidad
    data = codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final, cantidad_min, primer_ingreso, 0
    cursor.execute("INSERT INTO STOCKITEMS VALUES(NULL,?,?,?,?,?,?,?,?,?)", data)
    conex.commit()
    
    #ACTUALIZAR TABLA----------------------------------------------------------------------

def eliminar_articulo(id):
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    cursor.execute("DELETE FROM STOCKITEMS WHERE ID = " + str(id))
    conex.commit()
    messagebox.showinfo("Éxito", "Articulo eliminado correctamente!")
    #ACTUALIZAR TABLA----------------------------------------------------------------------

def get_datos():
    data_stock = []
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    cursor.execute("SELECT * FROM STOCKITEMS")
    datos = cursor.fetchall()
    for articulo in datos:
        data = [articulo[0], articulo[1], articulo[2], articulo[3], articulo[4], articulo[5], articulo[6], articulo[7], articulo[8], articulo[9]]
        data_stock.append(data)
    return data_stock

def modificar_articulo(id, codigo, nombre, cantidad, cantidad_min, precio_unit, porcent_ag, precio_final):
    modificar_ingresos(cantidad, id)
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    data = codigo, nombre, cantidad, cantidad_min, precio_unit, porcent_ag, precio_final
    cursor.execute("UPDATE STOCKITEMS SET CODIGO = ?, NOMBRE = ?, CANTIDAD = ?, CANTIDAD_MIN = ?, PRECIO_UNIT = ?, PORCENT_AG = ?, PRECIO_FINAL = ? WHERE id = " + str(id), data)
    conex.commit()
    messagebox.showinfo("Éxito", "Articulo modificado correctamente!")

def modificar_unidad(id, cantidad, opt):
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    cursor.execute("SELECT * FROM STOCKITEMS WHERE ID = " + str(id))
    dato = cursor.fetchall()
    cantidad_act = (dato[0][3])


    if opt == "inc":
        cant_inc = int(dato[0][8] + 1)
        data = cantidad, cant_inc, id
        cursor.execute("UPDATE STOCKITEMS SET CANTIDAD = ?, INGRESOS = ? WHERE id = ?", data)
        conex.commit()
        #print ("Cantidad: " + str(dato[0][3]) + ", ingresos: " + str(dato[0][8]) + ", salidas: " + str(dato[0][9]))
    elif opt == "dec":
        if dato[0][9] == None:
            cant_salida = 1
        else:
            cant_salida = int(dato[0][9] + 1)
        data = cantidad, cant_salida, id
        cursor.execute("UPDATE STOCKITEMS SET CANTIDAD = ?, SALIDAS = ? WHERE id = ?", data)
        conex.commit()
        #print ("Cantidad: " + str(cantidad_act-1) + ", ingresos: " + str(dato[0][8]) + ", salidas: " + str(cant_salida))


def modificar_ingresos(cantidad, id):
    nueva_cantidad = int(cantidad)
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    cursor.execute("SELECT * FROM STOCKITEMS WHERE ID = " + str(id))
    dato = cursor.fetchall()
    old_cantidad = int(dato[0][3])
    ingresos = int(dato[0][8])
    salidas = int(dato[0][9])
    
    if old_cantidad - nueva_cantidad < 0:
        flujo = ingresos + abs(nueva_cantidad - old_cantidad)
        data = flujo, id
        cursor.execute("UPDATE STOCKITEMS SET INGRESOS = ? WHERE id = ?", data)
        conex.commit()
    elif old_cantidad - nueva_cantidad > 0:
        flujo = salidas + (old_cantidad - nueva_cantidad)
        data = flujo, id
        cursor.execute("UPDATE STOCKITEMS SET SALIDAS = ? WHERE id = ?", data)
        conex.commit()
