from tkinter import *
from tkinter import ttk

class cantidad_window():
    def __init__(self):
        root = Tk()
        root.geometry("500x290")
        root.title("Modificar cantidad")
        root.config(bg="#C2CEE5")

        frame = Frame(root, width=500, height=300, bg="#C2CEE5")
        frame.pack(fill=BOTH)

        #Campos
        l1 = Label(frame, text="Código", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack(pady=10)
        e1 = Entry(frame, width= 30)
        e1.pack()


        l1 = Label(frame, text="Cantidad", bg="#C2CEE5", font = ('Helvetica', 12,'bold'))
        l1.pack(pady=10)
        e1 = Entry(frame, width= 30)
        e1.pack()


        b = Button(frame, text="Agregar cantidad(es)", width=30, bg= "#E6E2C3", bd= 1, font="Sans-serif")
        b.pack(pady=30)

        b = Button(frame, text="Eliminar cantidad(es)", width=30, bg= "#E6E2C3", bd= 1, font="Sans-serif")
        b.pack()

        root.mainloop()