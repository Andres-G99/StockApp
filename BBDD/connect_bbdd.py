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

def eliminar_articulo(codigo):
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    cursor.execute("DELETE FROM STOCKITEMS WHERE CODIGO =", codigo.get())
    conex.commit()
    messagebox.showinfo("Articulo eliminado correctamente!")
    #ACTUALIZAR TABLA----------------------------------------------------------------------

def get_datos():
    data_stock = []
    conex = sqlite3.connect("BBDD/stockBBDD.db")
    cursor = conex.cursor()
    cursor.execute("SELECT * FROM STOCKITEMS")
    datos = cursor.fetchall()
    for articulo in datos:
        data = [articulo[1], articulo[2], articulo[3], articulo[4], articulo[5], articulo[6]]
        data_stock.append(data)
    return data_stock

def modificar_articulo():
    pass

def agregar_cantidad():
    pass

def eliminar_cantidad():
    pass