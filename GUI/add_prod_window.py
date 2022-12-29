from tkinter import *
from tkinter import messagebox
from customtkinter import *
from Controller.app_functions import add_item, selected_record

class add_prod_window():
    def __init__(self, update):
        self.top = CTkToplevel()
        self.top.title("Agregar un producto")
        self.frame = CTkFrame(self.top, width=500, height=300, fg_color="#C2CEE5")
        self.frame.pack(fill=BOTH)
        self.update = update
    
        #Campos
        self.code = StringVar()
        self.name = StringVar()
        self.cantidad = StringVar()
        self.cantidad_min = StringVar()
        self.prec_u = StringVar()
        self.porc_ag = StringVar()

        l1 = CTkLabel(self.frame, text="Código", fg_color="#C2CEE5", text_color = 'black')
        l1.pack()
        e1 = CTkEntry(self.frame, width= 200, textvariable=self.code)
        e1.pack()

        l2 = CTkLabel(self.frame, text="Nombre", fg_color="#C2CEE5", text_color = 'black')
        l2.pack()
        e2 = CTkEntry(self.frame, width= 200, textvariable=self.name)
        e2.pack()

        l3 = CTkLabel(self.frame, text="Cantidad", fg_color="#C2CEE5", text_color = 'black')
        l3.pack()
        e3 = CTkEntry(self.frame, width= 200, textvariable=self.cantidad)
        self.cantidad.trace("w", self.on_validate_cant)
        e3.pack()

        l3_b = CTkLabel(self.frame, text="Cantidad Mínima", fg_color="#C2CEE5", text_color = 'black')
        l3_b.pack()
        e3_b = CTkEntry(self.frame, width= 200, textvariable=self.cantidad_min)
        self.cantidad_min.trace("w", self.on_validate_cm)
        e3_b.pack()

        l4 = CTkLabel(self.frame, text="Precio unitario", fg_color="#C2CEE5", text_color = 'black')
        l4.pack()
        e4 = CTkEntry(self.frame, width= 200, textvariable=self.prec_u)
        self.prec_u.trace("w", self.on_validate_prec)
        e4.pack()

        l5 = CTkLabel(self.frame, text="% Agregado", fg_color= "#C2CEE5", text_color = 'black')
        l5.pack()
        e5 = CTkEntry(self.frame, width= 200, textvariable=self.porc_ag)
        self.porc_ag.trace("w", self.on_validate_porc)
        e5.pack()

        b = CTkButton(self.frame, text="Agregar producto", width=200, command= self.enviar_datos)

        self.l_error = CTkLabel(self.frame, text="", fg_color= "pink", text_color = 'red')
        self.l_error.pack()
        
        b.pack(pady=20, padx= 20)

        global errores
        errores = []

    
    def enviar_datos(self):
        if self.check_var():
            self.update(self.code.get(), self.name.get(), int(self.cantidad.get()), int(self.cantidad_min.get()), float(self.prec_u.get()), float(self.porc_ag.get()))
            self.top.destroy()

    def on_validate_cant(self,*args):
        if all(c in "01234567890" for c in self.cantidad.get()):
            if "cantidad" in errores:
                errores.remove("cantidad")
        else:
            if "cantidad" not in errores:
                errores.append("cantidad")
        self.string_error(errores)

    def on_validate_cm(self,*args):
        if all(c in "01234567890" for c in self.cantidad_min.get()):
            if "cantidad mínima" in errores:
                errores.remove("cantidad mínima")
        else:
            if "cantidad mínima" not in errores:
                errores.append("cantidad mínima")
        self.string_error(errores)

    def on_validate_prec(self,*args):
        if all(c in "01234567890." for c in self.prec_u.get()):
            if "precio unitario" in errores:
                errores.remove("precio unitario")
        else:
            if "precio unitario" not in errores:
                errores.append("precio unitario")
        self.string_error(errores)

    def on_validate_porc(self,*args):
        if all(c in "01234567890." for c in self.porc_ag.get()):
            if "% agregado" in errores:
                errores.remove("% agregado")
        else:
            if "% agregado" not in errores:
                errores.append("% agregado")
        self.string_error(errores)

    def string_error(self, errores):
        string = "Por favor, corrija: "
        if len(errores) != 0:
            for error in errores:
                string = string + "\n# Error en: " + str(error)
            
            self.l_error.configure(text = "")
            self.l_error.configure(text = string)
        else:
            self.l_error.configure(text = "")


    def check_var(self):
        if len(errores) == 0:
            datos = self.code.get(), self.name.get(), self.cantidad.get(), self.cantidad_min.get(), self.prec_u.get(), self.porc_ag.get()
            for dato in datos:
                if dato == "":
                    messagebox.showerror("Error de entrada", "Debe completar TODOS los campos")
                    self.top.deiconify()
                    return False
            return True
        else:
            messagebox.showerror("Error de entrada", "Por favor, corrija los errores")
            self.top.deiconify()
            return False