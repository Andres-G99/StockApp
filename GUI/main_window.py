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
        bottom_frame = CTkFrame(root, width=w, height=(h*0.1), border_color = ("blue"), border_width=2)
        bottom_frame.pack(expand=True, side='bottom', fill=BOTH)
        bottom_frame.configure(fg_color="#80d8ff")

        butt_modif = CTkButton(bottom_frame, text="Modificar", width=150, command=self.new_modfW)
        butt_add_u = CTkButton(bottom_frame, text="Agregar unidad", width=150,  command=self.add_unidad)
        butt_elim_u = CTkButton(bottom_frame, text="Eliminar unidad", width=150,  command=self.del_unidad)
        butt_stats = CTkButton(bottom_frame, text="Ver Estadísticas", width=150,  command=self.new_stats)
        butt_imp = CTkButton(bottom_frame, text="Importar de Excel", fg_color="green", width=150,  command=imp_data)

        butt_modif.place(relx= (0.20), rely= (0.35))
        butt_add_u.place(relx= (0.325), rely= (0.35))
        butt_elim_u.place(relx= (0.45), rely= (0.35))
        butt_stats.place(relx= (0.575), rely= (0.35))
        butt_imp.place(relx= (0.7), rely= (0.35))

        #PANEL IZQUIERDO
        left_frame = CTkFrame(root, width=(w*0.05), height=(h*0.8), border_color = ("lightgreen","green"), border_width=2)
        left_frame.pack(expand=True, side='left', fill=BOTH)
        left_frame.configure(fg_color="#a5ee9d")
        

        butt_add_prod = CTkButton(left_frame, text="Agregar Producto", width= 200, command= self.new_addw)
        #butt_add_prod.place(x= (((w*0.2)/2) - 80), y= (40))  # p = x/2 - l
        butt_add_prod.place(relx= (0.20), rely= (0.10))

        butt_elim_prod = CTkButton(left_frame, text="Eliminar Producto", width= 200, command=self.eliminar_registro)
        # butt_elim_prod.place(x= (((w*0.2)/2) - 80), y=(100))
        butt_elim_prod.place(relx= (0.20), rely= (0.175))

        lista_param = CTkComboBox(left_frame, width= 200, values=["Todos","Por nombre", "Por código"], variable=self.opcion)
        lista_param.set("Todos")
        # lista_param.place(x= (((w*0.2)/2) - 80), y=(h*0.5))
        lista_param.place(relx= (0.20), rely= (0.6))

        barra_busqueda = CTkEntry(left_frame, width=190, textvariable=self.barra_param)
        # barra_busqueda.place(x= (((w*0.2)/2) - 80), y=(h*0.5 + 40))
        barra_busqueda.place(relx= (0.20), rely= (0.65))

        Btn_desh = CTkButton(left_frame, text="X", width=3, command=self.deshacer_busqueda)
        Btn_desh.place(relx= (0.75), rely= (0.65))

        butt_busqueda = CTkButton(left_frame, text="Buscar", width=200, command=self.search)
        butt_busqueda.place(relx= (0.20), rely= (0.7))

        #PANEL DERECHO
        global right_frame
        #right_frame = CTkFrame(root, width=(w*0.8), height=(h*0.8))
        right_frame = CTkFrame(root, border_color = ("black"), border_width=2, width = (w*0.95))
        right_frame.pack(side='right')
        right_frame.configure(fg_color="#b0bec5")
        crear_tabla(right_frame, False, None)

        root.after(1000, func = None)
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
    
