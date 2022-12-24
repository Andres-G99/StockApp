from tkinter import *
from tkinter import ttk

class stats_window():
    def __init__(self):
        top = Toplevel()
        self.frame = Frame(top, width=500, height=300, bg="#C2CEE5")
        self.frame.pack(fill=BOTH)


        self.tabla_stats = ttk.Treeview(self.frame, height=100)
        self.tabla_stats.pack()
        self.tabla_stats['columns'] = ('Id', 'Codigo', 'Nombre', 'Cantidad', 'Ingresos', 'Salidas', 'Estado')

        self.tabla_stats.tag_configure("sin_stock", background = "#E57373")
        self.tabla_stats.tag_configure("reponer", background = "#FFB74D")
        self.tabla_stats.tag_configure("en_stock", background = "white" )

        self.tabla_stats.column("#0", stretch = NO, width=1)
        self.tabla_stats.column("Id", stretch = NO, width=1)
        self.tabla_stats.column("Codigo", width=200, minwidth= 190)
        self.tabla_stats.column("Nombre", width=300, minwidth= 290)
        self.tabla_stats.column("Cantidad", width=170, minwidth= 160)
        self.tabla_stats.column("Ingresos", width=170, minwidth= 160)
        self.tabla_stats.column("Salidas", width=170, minwidth= 160)  
        self.tabla_stats.column("Estado", width=170, minwidth= 160)

        self.tabla_stats.heading("#0", text="")
        self.tabla_stats.heading("Id", text="Id")
        self.tabla_stats.heading("Codigo", text="Código")
        self.tabla_stats.heading("Nombre", text="Nombre")
        self.tabla_stats.heading("Cantidad", text="Cantidad")
        self.tabla_stats.heading("Ingresos", text="Ingresos")
        self.tabla_stats.heading("Salidas", text="Salidas")
        self.tabla_stats.heading("Estado", text="Estado")

        self.tabla_stats.insert(parent='', index='end', id = 0, values=("0","Retx", "Retén X", "0", "10", "10", "SIN STOCK"), tag = "sin_stock")
        self.tabla_stats.insert(parent='', index='end', id = 1, values=("0","Rety", "Retén Y", "4", "12", "8", "REPONER"), tag = "reponer")
        self.tabla_stats.insert(parent='', index='end', id = 2, values=("0","Retz", "Retén Z", "7", "14", "7", "EN STOCK"), tag = "en_stock")