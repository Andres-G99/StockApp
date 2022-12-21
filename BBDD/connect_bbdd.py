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
            PRECIO_FINAL FLOAT(15))
        ''')
    except:
        messagebox.showwarning("Error BBDD", "La BBDD ya existe")
        print("Error con la bbdd")

def insertar_articulo(codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final):
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    data = codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final
    cursor.execute("INSERT INTO STOCKITEMS VALUES(NULL,?,?,?,?,?,?)", data)
    conex.commit()
    messagebox.showinfo("Éxito","Articulo guardado correctamente!")
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
        data = [articulo[0], articulo[1], articulo[2], articulo[3], articulo[4], articulo[5], articulo[6]]
        data_stock.append(data)
    return data_stock

def modificar_articulo(id, codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final):
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    data = codigo, nombre, cantidad, precio_unit, porcent_ag, precio_final
    cursor.execute("UPDATE STOCKITEMS SET CODIGO = ?, NOMBRE = ?, CANTIDAD = ?, PRECIO_UNIT = ?, PORCENT_AG = ?, PRECIO_FINAL = ? WHERE id = " + str(id), data)
    conex.commit()
    messagebox.showinfo("Éxito", "Articulo modificado correctamente!")

def modificar_unidad(id, cantidad):
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    data = cantidad, id
    cursor.execute("UPDATE STOCKITEMS SET CANTIDAD = ? WHERE id = ?", data)
    conex.commit()
