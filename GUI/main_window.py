from tkinter import *
from tkinter import ttk
from customtkinter import CTkButton
from customtkinter import *

from GUI.cantidad_window import *
from GUI.add_prod_window import add_prod_window
from GUI.modif_window import modif_window
from BBDD.connect_bbdd import *
from Controller.app_functions import crear_tabla, selected_record
from Controller.app_functions import add_item, remove_record, update_record, increment_record, decrement_record, buscar, destruir_tabla, selected_record, imp_data, reload_tabla
from GUI.stats_window import stats_window

class main_window():
    def __init__(self):
        root = CTk()
        root.state('zoomed')
        root.title("StockApp")
        root.configure(fg_color='#b0bec5')
        self.barra_param = StringVar()
        self.opcion = StringVar()
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()

        root.geometry(str(w) + "x" + str(h))
        #root.minsize("1024x768")
        root.minsize(height=768, width=1024)

        #PANEL INFERIOR
        self.bottom_frame = CTkFrame(root, width=w, height=(h*0.1), border_color = ("blue"), border_width=2)
        self.bottom_frame.pack(expand=True, side='bottom', fill=BOTH)
        self.bottom_frame.configure(fg_color="#80d8ff")

        self.butt_modif = CTkButton(self.bottom_frame, text="Modificar", width=150, command=self.new_modfW)
        self.butt_add_u = CTkButton(self.bottom_frame, text="Agregar unidad", width=150,  command=self.add_unidad)
        self.butt_elim_u = CTkButton(self.bottom_frame, text="Eliminar unidad", width=150,  command=self.del_unidad)
        self.butt_stats = CTkButton(self.bottom_frame, text="Ver Estadísticas", width=150,  command=self.new_stats)
        self.butt_imp = CTkButton(self.bottom_frame, text="Importar de Excel", fg_color="green", width=150,  command=imp_data)

        self.butt_modif.place(relx= (0.20), rely= (0.35))
        self.butt_add_u.place(relx= (0.325), rely= (0.35))
        self.butt_elim_u.place(relx= (0.45), rely= (0.35))
        self.butt_stats.place(relx= (0.575), rely= (0.35))
        self.butt_imp.place(relx= (0.7), rely= (0.35))

        #PANEL IZQUIERDO
        self.left_frame = CTkFrame(root, width=(w*0.05), height=(h*0.8), border_color = ("lightgreen","green"), border_width=2)
        self.left_frame.pack(expand=True, side='left', fill=BOTH)
        self.left_frame.configure(fg_color="#a5ee9d")
        

        self.butt_add_prod = CTkButton(self.left_frame, text="Agregar Producto", width= 200, command= self.new_addw)
        #butt_add_prod.place(x= (((w*0.2)/2) - 80), y= (40))  # p = x/2 - l
        self.butt_add_prod.place(relx= (0.20), rely= (0.10))

        self.butt_elim_prod = CTkButton(self.left_frame, text="Eliminar Producto", width= 200, command=self.eliminar_registro)
        # butt_elim_prod.place(x= (((w*0.2)/2) - 80), y=(100))
        self.butt_elim_prod.place(relx= (0.20), rely= (0.175))

        self.lista_param = CTkComboBox(self.left_frame, width= 200, values=["Todos","Por nombre", "Por código"], variable=self.opcion)
        self.lista_param.set("Todos")
        # lista_param.place(x= (((w*0.2)/2) - 80), y=(h*0.5))
        self.lista_param.place(relx= (0.20), rely= (0.6))

        self.barra_busqueda = CTkEntry(self.left_frame, width=190, textvariable=self.barra_param)
        # barra_busqueda.place(x= (((w*0.2)/2) - 80), y=(h*0.5 + 40))
        self.barra_busqueda.place(relx= (0.20), rely= (0.65))

        self.Btn_desh = CTkButton(self.left_frame, text="X", width=3, command=self.deshacer_busqueda)
        self.Btn_desh.place(relx= (0.75), rely= (0.65))

        self.butt_busqueda = CTkButton(self.left_frame, text="Buscar", width=200, command=self.search)
        self.butt_busqueda.place(relx= (0.20), rely= (0.7))

        #PANEL DERECHO
        global right_frame
        #right_frame = CTkFrame(root, width=(w*0.8), height=(h*0.8))
        right_frame = CTkFrame(root, border_color = ("black"), border_width=2, width = (w*0.95))
        right_frame.pack(side='right')
        right_frame.configure(fg_color="#b0bec5")
        crear_tabla(right_frame, False, None)

        root.mainloop()


    def update(self, code, name, cantidad, cantidad_min, prec_u, porc_ag):
        add_item(code, name, cantidad, cantidad_min, prec_u, porc_ag)
        crear_tabla(right_frame, False, None)

    def new_addw(self):
        m = add_prod_window(self.update)

    def new_stats(self):
        s = stats_window()

    def new_modfW(self):
        if selected_record() == '':
            messagebox.showerror("Error","Debe seleccionar un articulo primero")
        else:
            mw = modif_window(self.modificar_registro)


    def eliminar_registro(self):
        if selected_record() == '':
            messagebox.showerror("Error","Debe seleccionar un articulo primero")
        else:
            remove_record()

    def modificar_registro(self, id, code, name, cantidad, cantidad_min, prec_u, porc_ag):
        update_record(id, code, name, cantidad, cantidad_min, prec_u, porc_ag)
        #crear_tabla(right_frame)

    def add_unidad(self):
        if selected_record() == '':
            messagebox.showerror("Error","Debe seleccionar un articulo primero")
        else:
            increment_record()
    
    def del_unidad(self):
        if selected_record() == '':
            messagebox.showerror("Error","Debe seleccionar un articulo primero")
        else:
            decrement_record()

    def search(self):
        result = buscar(self.barra_param.get(), self.opcion.get())

    def deshacer_busqueda(self):
        reload_tabla()
    

    def color_mk(self):
            #PANEL IZQUIERDO
            self.left_frame.configure(fg_color="#EF9A9A", border_color = "#EF9A9A")
            self.butt_add_prod.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
            self.butt_elim_prod.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
            self.butt_busqueda.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
            self.Btn_desh.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
            #PANEL INFERIOR
            self.bottom_frame.configure(fg_color="#C2185B", border_color = "#AD1457")
            self.butt_modif.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
            self.butt_add_u.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
            self.butt_elim_u.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
            self.butt_stats.configure(border_width = 2, fg_color = "white", text_color = "black", hover_color = "#BDBDBD")
            self.butt_imp.configure(border_width = 2, fg_color = "#689f38", text_color = "white", hover_color = "#BDBDBD")