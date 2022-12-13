from tkinter import *
from tkinter import ttk

class add_prod_window():
    def __init__(self):
        root = Tk()
        root.geometry("500x290")
        root.title("Agregar producto")

        frame = Frame(root, width=500, height=300, bg="#C2CEE5")
        frame.pack(fill=BOTH)

        #Campos
        l1 = Label(frame, text="Código", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack()
        e1 = Entry(frame, width= 30)
        e1.pack()

        l1 = Label(frame, text="Nombre", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack()
        e1 = Entry(frame, width= 30)
        e1.pack()

        l1 = Label(frame, text="Cantidad", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack()
        e1 = Entry(frame, width= 30)
        e1.pack()

        l1 = Label(frame, text="Precio unitario", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack()
        e1 = Entry(frame, width= 30)
        e1.pack()

        l1 = Label(frame, text="% Agregado", bg= "#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack()
        e1 = Entry(frame, width= 30)
        e1.pack()

        b = Button(frame, text="Agregar producto", width=30, bg= "#E6E2C3", bd= 1, font="Sans-serif")
        b.pack(pady=20)

        root.mainloop()