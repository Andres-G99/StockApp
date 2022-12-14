from tkinter import *
from tkinter import ttk
from customtkinter import *
from Controller.app_functions import ordenar_por_salida, ordenar_por_faltantes, exp_data, print_data
import firebase_admin
from firebase_admin import db


class stats_window():
    def __init__(self):
        self.top = CTkToplevel(fg_color="black")
        self.top.title("Estado del stock")
        global frame
        self.frame = CTkFrame(self.top, width=500, height=100, fg_color="#C2CEE5", border_width=2)
        self.frame.pack(fill=BOTH, side='bottom')
        self.tb = self.crear_tabla_stats(self.frame)

        

        self.frame_btn = CTkFrame(self.top, fg_color="#C2CEE5", border_width=2)
        self.frame_btn.pack(expand=False, side='top', fill = BOTH)
        self.label_btn =  CTkLabel(self.frame_btn, text="Ordenar por: ", fg_color="#C2CEE5", height = 10, text_color="black")
        self.btn_ord1 =  CTkButton(self.frame_btn, text="Faltantes", width=100, height = 10, command=self.ord_faltantes)
        self.btn_ord2 =  CTkButton(self.frame_btn, text="Salida", width=100, height = 10, command=self.ord_salida)
        self.btn_exp =  CTkButton(self.frame_btn, text="Exportar a Excel", width=100, height = 10, command=exp_data)
        self.btn_print =  CTkButton(self.frame_btn, text="Imprimir", width=100, height = 10, command=print_data)
        self.label_btn.grid(row=0, column=0, pady= 2, padx = 2)
        self.btn_ord1.grid(row=0, column=1, pady= 2)
        self.btn_ord2.grid(row=0, column=2, pady= 2)
        self.btn_exp.grid(row=0, column=3, pady= 2)
        self.btn_print.grid(row=0, column=4, pady= 2)


        self.cargar_tabla(self.tb, "faltantes")

        

    def crear_tabla_stats(self, frame):
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,'bold')) 
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        self.sb = CTkScrollbar(frame)
        self.sb.pack(side=RIGHT, fill=Y, padx=2, pady=5)

        self.tabla_stats = ttk.Treeview(frame, height=30, yscrollcommand=self.sb.set, style="mystyle.Treeview")
        self.tabla_stats.pack(padx=5, pady=5)
        self.tabla_stats['columns'] = ('Codigo', 'Nombre', 'Cantidad', 'Ingresos', 'Salidas', 'Estado')
        self.sb.configure(command=self.tabla_stats.yview)

        self.tabla_stats.tag_configure("sin_stock_par", background = "#ff8164")
        self.tabla_stats.tag_configure("sin_stock_impar", background = "#ffa590")

        self.tabla_stats.tag_configure("reponer_par", background = "#f1b04c")
        self.tabla_stats.tag_configure("reponer_impar", background = "#f5c77e")

        self.tabla_stats.tag_configure("en_stock_par", background = "#83f28f")
        self.tabla_stats.tag_configure("en_stock_impar", background = "#abf7b1")

        self.tabla_stats.column("#0", stretch = NO, width=1)
        #self.tabla_stats.column("Id", stretch = NO, width=1)
        self.tabla_stats.column("Codigo", width=200, minwidth= 190)
        self.tabla_stats.column("Nombre", width=300, minwidth= 290)
        self.tabla_stats.column("Cantidad", width=170, minwidth= 160)
        self.tabla_stats.column("Ingresos", width=170, minwidth= 160)
        self.tabla_stats.column("Salidas", width=170, minwidth= 160)  
        self.tabla_stats.column("Estado", width=170, minwidth= 160)

        self.tabla_stats.heading("#0", text="")
        #self.tabla_stats.heading("Id", text="Id")
        self.tabla_stats.heading("Codigo", text="C??digo")
        self.tabla_stats.heading("Nombre", text="Nombre")
        self.tabla_stats.heading("Cantidad", text="Cantidad")
        self.tabla_stats.heading("Ingresos", text="Ingresos")
        self.tabla_stats.heading("Salidas", text="Salidas")
        self.tabla_stats.heading("Estado", text="Estado")

        return self.tabla_stats
        

    def cargar_tabla(self, tabla_st, opt):

        if opt == "faltantes":
            datos = ordenar_por_faltantes()
        elif opt == "salida":
            datos = ordenar_por_salida()
        #datos = ordenar_por_salida()
        iter = 0
        for dato in datos:
            
            if dato.get("CANTIDAD") >= int(dato.get("CANTIDAD_MIN")): #CANTIDAD > CANT MIN
                if iter % 2 == 0:
                    self.tabla_stats.insert(parent='', index='end', id = iter, values=(dato.get("CODIGO"), dato.get("NOMBRE"), dato.get("CANTIDAD"), dato.get("INGRESOS"), dato.get("SALIDAS"), "STOCK"), tag = "en_stock_par")
                    iter = iter + 1
                else:
                    self.tabla_stats.insert(parent='', index='end', id = iter, values=(dato.get("CODIGO"), dato.get("NOMBRE"), dato.get("CANTIDAD"), dato.get("INGRESOS"), dato.get("SALIDAS"), "STOCK"), tag = "en_stock_impar")
                    iter = iter + 1

            elif dato.get("CANTIDAD") == 0:
                if iter % 2 == 0:
                    self.tabla_stats.insert(parent='', index='end', id = iter, values=(dato.get("CODIGO"), dato.get("NOMBRE"), dato.get("CANTIDAD"), dato.get("INGRESOS"), dato.get("SALIDAS"), "SIN STOCK ["+ str(dato.get("CANTIDAD_MIN"))+"]"), tag = "sin_stock_par")
                    iter = iter + 1
                else:
                    self.tabla_stats.insert(parent='', index='end', id = iter, values=(dato.get("CODIGO"), dato.get("NOMBRE"), dato.get("CANTIDAD"), dato.get("INGRESOS"), dato.get("SALIDAS"), "SIN STOCK ["+ str(dato.get("CANTIDAD_MIN"))+"]"), tag = "sin_stock_impar")
                    iter = iter + 1

            elif dato.get("CANTIDAD") < int(dato.get("CANTIDAD_MIN")): #CANTIDAD < CANT MIN
                if iter % 2 == 0:
                    cant_rep = dato.get("CANTIDAD_MIN") - dato.get("CANTIDAD")
                    self.tabla_stats.insert(parent='', index='end', id = iter, values=(dato.get("CODIGO"), dato.get("NOMBRE"), dato.get("CANTIDAD"), dato.get("INGRESOS"), dato.get("SALIDAS"), "REPONER " + str(cant_rep)), tag = "reponer_par")
                    iter = iter + 1
                else:
                    cant_rep = dato.get("CANTIDAD_MIN") - dato.get("CANTIDAD")
                    self.tabla_stats.insert(parent='', index='end', id = iter, values=(dato.get("CODIGO"), dato.get("NOMBRE"), dato.get("CANTIDAD"), dato.get("INGRESOS"), dato.get("SALIDAS"), "REPONER " + str(cant_rep)), tag = "reponer_impar")
                    iter = iter + 1

    def reset_tabla(self, tb):
        for i in self.tb.get_children():
            self.tb.delete(i)

    def ord_faltantes(self):
        self.reset_tabla(self.tb)
        self.cargar_tabla(self.tb, "faltantes")

    def ord_salida(self):
        self.reset_tabla(self.tb)
        self.cargar_tabla(self.tb, "salida")
        #ordenar_por_salida()


    def color_mk_stats(self):
        self.frame.configure(fg_color= "pink")
        self.frame_btn.configure(fg_color= "pink")
        self.label_btn.configure(fg_color= "pink")
        self.btn_ord1.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
        self.btn_ord2.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
        self.btn_print.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
        self.btn_exp.configure(border_width = 2, fg_color = "#689f38", text_color = "white", hover_color = "#BDBDBD")