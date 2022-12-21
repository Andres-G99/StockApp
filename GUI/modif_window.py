from tkinter import *
from Controller.app_functions import add_item, selected_record

class modif_window():
    def __init__(self, modificar_registro):
        top = Toplevel()
        self.frame = Frame(top, width=500, height=300, bg="#C2CEE5")
        self.frame.pack(fill=BOTH)
        values = selected_record()
        self.modificar_registro = modificar_registro

    
        #Campos
        self.id = values[0]
        self.code = StringVar()
        self.name = StringVar()
        self.cantidad = IntVar()
        self.prec_u = IntVar()
        self.porc_ag = IntVar()


        l1 = Label(self.frame, text="Código", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack()
        e1 = Entry(self.frame, width= 30, textvariable=self.code)
        e1.insert(0, values[1])
        e1.pack()

        l2 = Label(self.frame, text="Nombre", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l2.pack()
        e2 = Entry(self.frame, width= 30, textvariable=self.name)
        e2.insert(0, values[2])
        e2.pack()

        l3 = Label(self.frame, text="Cantidad", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l3.pack()
        e3 = Entry(self.frame, width= 30, textvariable=self.cantidad)
        e3.insert(0, values[3])
        e3.pack()

        l4 = Label(self.frame, text="Precio unitario", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l4.pack()
        e4 = Entry(self.frame, width= 30, textvariable=self.prec_u)
        e4.insert(0, values[4])
        e4.pack()

        l5 = Label(self.frame, text="% Agregado", bg= "#C2CEE5", font = ('Helvetica', 12,'bold'))
        l5.pack()
        e5 = Entry(self.frame, width= 30, textvariable=self.porc_ag)
        e5.insert(0, values[5])
        e5.pack()

        b = Button(self.frame, text="Modificar", width=20, bg= "#E6E2C3", bd= 1, font="Sans-serif", command=self.modificar_datos)

        b.pack(pady=20)




    def modificar_datos(self):
        self.modificar_registro(self.id, self.code.get(), self.name.get(), self.cantidad.get(), self.prec_u.get(), self.porc_ag.get())
