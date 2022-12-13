from tkinter import Button

class boton_prop():
    def __init__(self, frame, texto, width):
        b = Button(self, frame, text = texto, width = width, bg= "#E6E2C3", bd= 1, font="Sans-serif")
