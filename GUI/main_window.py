from tkinter import *
from tkinter import ttk

class main_window():
    def __init__(self):
        root = Tk()
        
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()

        root.geometry(str(w) + "x" + str(h))

        #PANEL INFERIOR
        bottom_frame = Frame(root, width=w, height=(h*0.2))
        bottom_frame.pack(expand=True, side='bottom', fill=X)
        bottom_frame.config(background="#80d8ff")
        bottom_frame.grid_propagate(False)

        butt_modif = Button(bottom_frame, text="Modificar")
        butt_add_u = Button(bottom_frame, text="Agregar unidad")
        butt_elim_u = Button(bottom_frame, text="Eliminar unidad")
        butt_add_elim_cant = Button(bottom_frame, text="Agregar/Eliminar cantidad")

        butt_modif.grid(row=0, column=0, padx=5, pady=5)
        butt_add_u.grid(row=0, column=1, padx=5, pady=5)
        butt_elim_u.grid(row=0, column=2, padx=5, pady=5)
        butt_add_elim_cant.grid(row=0, column=3, padx=5, pady=5)

        #PANEL IZQUIERDO
        left_frame = Frame(root, width=(w*0.2), height=(h*0.8))
        left_frame.pack(expand=True, side='left', fill=BOTH)
        left_frame.config(background="#a5ee9d")
        

        butt_add_prod = Button(left_frame, text="Agregar Producto", width= 20)
        butt_add_prod.place(x= (((w*0.2)/2) - 80), y= (40))  # p = x/2 - l
        

        butt_elim_prod = Button(left_frame, text="Eliminar Producto", width= 20)
        butt_elim_prod.place(x= (((w*0.2)/2) - 80), y=(80))

        lista_param = ttk.Combobox(left_frame, width= 20)
        lista_param.place(x= (((w*0.2)/2) - 80), y=(h*0.5))

        barra_busqueda = Entry(left_frame, width=24)
        barra_busqueda.place(x= (((w*0.2)/2) - 80), y=(h*0.5 + 40))

        butt_busqueda = Button(left_frame, text="Buscar", width=20)
        butt_busqueda.place(x= (((w*0.2)/2) - 80), y=(h*0.5 + 80))

        #PANEL DERECHO
        right_frame = Frame(root, width=(w*0.8), height=(h*0.8))
        right_frame.pack(expand=True, side='right', fill=BOTH)
        right_frame.config(background="#b0bec5")
        crear_tabla(self, right_frame)
        


        root.mainloop()
    

def crear_tabla(self, frame):
    param = ["Codigo", "Nombre", "Cantidad", "Precio unitario", "% Agregado", "Precio final"]
    for k in range(6):
        if param[k] == "Codigo":
            self.e = Entry(frame, width=20)
            self.e.grid(row= 0, column= k)
            self.e.insert(END, param[k])
        elif param[k] == "Nombre":
            self.e = Entry(frame, width=50)
            self.e.grid(row= 0, column= k)
            self.e.insert(END, param[k])
        else:
            self.e = Entry(frame, width=30)
            self.e.grid(row= 0, column= k)
            self.e.insert(END, param[k])    

    for i in range(1,31):
        for j in range(6):
            if param[j] == "Codigo":
                self.e = Entry(frame, width=20)
                self.e.grid(row=i, column= j)
            elif param[j] == "Nombre":
                self.e = Entry(frame, width=50)
                self.e.grid(row=i, column= j)
            else:
                self.e = Entry(frame, width=30)
                self.e.grid(row=i, column= j)
