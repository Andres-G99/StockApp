from tkinter import *
from tkinter import ttk

class main_window():
    def __init__(self):
        root = Tk()

        root.title("StockApp")
        
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()

        root.geometry(str(w) + "x" + str(h))
        #root.minsize("1024x768")
        root.minsize(height=768, width=1024)

        #PANEL INFERIOR
        bottom_frame = Frame(root, width=w, height=(h*0.1))
        bottom_frame.pack(expand=True, side='bottom', fill=BOTH)
        bottom_frame.config(background="#80d8ff")

        butt_modif = Button(bottom_frame, text="Modificar", width=20, bg= "#E6E2C3", bd= 1, font="Sans-serif")
        butt_add_u = Button(bottom_frame, text="Agregar unidad", width=20, bg= "#E6E2C3", bd= 1, font="Sans-serif")
        butt_elim_u = Button(bottom_frame, text="Eliminar unidad", width=20, bg= "#E6E2C3", bd= 1, font="Sans-serif")
        butt_add_elim_cant = Button(bottom_frame, text="Agregar/Eliminar cantidad", width=20, bg= "#E6E2C3", bd= 1, font="Sans-serif")

        butt_modif.place(x= (w*0.2), y= (30))
        butt_add_u.place(x= (w*0.2 + 200), y= (30))
        butt_elim_u.place(x= (w*0.2 + 400), y= (30))
        butt_add_elim_cant.place(x= (w*0.2 + 600), y= (30))

        #PANEL IZQUIERDO
        left_frame = Frame(root, width=(w*0.2), height=(h*0.8))
        left_frame.pack(expand=True, side='left', fill=BOTH)
        left_frame.config(background="#a5ee9d")
        

        butt_add_prod = Button(left_frame, text="Agregar Producto", width= 20, bg= "#E6E2C3", bd= 1, font="Sans-serif")
        butt_add_prod.place(x= (((w*0.2)/2) - 80), y= (40))  # p = x/2 - l
        

        butt_elim_prod = Button(left_frame, text="Eliminar Producto", width= 20, bg= "#E6E2C3", bd= 1, font="Sans-serif")
        butt_elim_prod.place(x= (((w*0.2)/2) - 80), y=(100))

        lista_param = ttk.Combobox(left_frame, width= 30)
        lista_param.place(x= (((w*0.2)/2) - 80), y=(h*0.5))

        barra_busqueda = Entry(left_frame, width=30)
        barra_busqueda.place(x= (((w*0.2)/2) - 80), y=(h*0.5 + 40))

        butt_busqueda = Button(left_frame, text="Buscar", width=20, bg= "#E6E2C3", bd= 1, font="Sans-serif")
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
            #self.e = Entry(frame, width=20)
            self.e = Text(frame, width=15, height=1)
            self.e.grid(row= 0, column= k)
            self.e.insert(END, param[k])
            self.e.config(state=DISABLED)
        elif param[k] == "Nombre":
            #self.e = Entry(frame, width=50)
            self.e = Text(frame, width=30, height=1)
            self.e.grid(row= 0, column= k)
            self.e.insert(END, param[k])
            self.e.config(state=DISABLED)
        else:
            #self.e = Entry(frame, width=30)
            self.e = Text(frame, width=20, height=1)
            self.e.grid(row= 0, column= k)
            self.e.insert(END, param[k])
            self.e.config(state=DISABLED)   

    for i in range(1,30):
        for j in range(6):
            if param[j] == "Codigo":
                self.e = Text(frame, width=15, height=1)
                self.e.grid(row=i, column= j)
            elif param[j] == "Nombre":
                self.e = Text(frame, width=30, height=1)
                self.e.grid(row=i, column= j)
            else:
                self.e = Text(frame, width=20, height=1)
                self.e.grid(row=i, column= j)
