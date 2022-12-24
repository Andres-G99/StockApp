from tkinter import *
from Controller.app_functions import add_item, selected_record

class add_prod_window():
    def __init__(self, update):
        top = Toplevel()
        self.frame = Frame(top, width=500, height=300, bg="#C2CEE5")
        self.frame.pack(fill=BOTH)
        self.update = update
    
        #Campos
        self.code = StringVar()
        self.name = StringVar()
        self.cantidad = IntVar()
        self.cantidad_min = IntVar()
        self.prec_u = IntVar()
        self.porc_ag = IntVar()

        l1 = Label(self.frame, text="Código", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack()
        e1 = Entry(self.frame, width= 30, textvariable=self.code)
        e1.pack()

        l2 = Label(self.frame, text="Nombre", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l2.pack()
        e2 = Entry(self.frame, width= 30, textvariable=self.name)
        e2.pack()

        l3 = Label(self.frame, text="Cantidad", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l3.pack()
        e3 = Entry(self.frame, width= 30, textvariable=self.cantidad)
        e3.pack()

        l3_b = Label(self.frame, text="Cantidad Mínima", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l3_b.pack()
        e3_b = Entry(self.frame, width= 30, textvariable=self.cantidad_min)
        e3_b.pack()

        l4 = Label(self.frame, text="Precio unitario", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l4.pack()
        e4 = Entry(self.frame, width= 30, textvariable=self.prec_u)
        e4.pack()

        l5 = Label(self.frame, text="% Agregado", bg= "#C2CEE5", font = ('Helvetica', 12,'bold'))
        l5.pack()
        e5 = Entry(self.frame, width= 30, textvariable=self.porc_ag)
        e5.pack()

        b = Button(self.frame, text="Agregar producto", width=20, bg= "#E6E2C3", bd= 1, font="Sans-serif", command= self.enviar_datos)
        
        b.pack(pady=20)



    
    def enviar_datos(self):
        self.update(self.code.get(), self.name.get(), self.cantidad.get(), self.cantidad_min.get(), self.prec_u.get(), self.porc_ag.get())
