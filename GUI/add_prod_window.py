from tkinter import *
from tkinter import ttk
from Controller.app_functions import add_item

class add_prod_window():
    def __init__(self):
        root = Tk()
        root.geometry("500x290")
        root.title("Agregar producto")

        frame = Frame(root, width=500, height=300, bg="#C2CEE5")
        frame.pack(fill=BOTH)

        #Campos

        code = StringVar()
        name = StringVar()
        cantidad = IntVar()
        prec_u = IntVar()
        porc_ag = IntVar()


        l1 = Label(frame, text="Código", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack()
        e1 = Entry(frame, width= 30, textvariable=code)
        e1.pack()

        l2 = Label(frame, text="Nombre", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l2.pack()
        e2 = Entry(frame, width= 30, textvariable=name)
        e2.pack()

        l3 = Label(frame, text="Cantidad", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l3.pack()
        e3 = Entry(frame, width= 30, textvariable=cantidad)
        e3.pack()

        l4 = Label(frame, text="Precio unitario", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l4.pack()
        e4 = Entry(frame, width= 30, textvariable=prec_u)
        e4.pack()

        l5 = Label(frame, text="% Agregado", bg= "#C2CEE5", font = ('Helvetica', 12,'bold'))
        l5.pack()
        e5 = Entry(frame, width= 30, textvariable=porc_ag)
        e5.pack()

        b = Button(frame, text="Agregar producto", width=30, bg= "#E6E2C3", bd= 1, font="Sans-serif", command= lambda:enviar_datos(code, name, cantidad, prec_u, porc_ag))
        b.pack(pady=20)



        root.mainloop()


    
def enviar_datos(code, name, cantidad, prec_u, porc_ag):
        cod = code.get()
        nm = name.get()
        cant = cantidad.get()
        p_u = prec_u.get()
        p_ag = porc_ag.get()

        add_item(cod, nm, cant, p_u, p_ag)
