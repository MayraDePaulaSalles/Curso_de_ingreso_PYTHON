import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mayra
apellido: De Paula Salles
---
Ejercicio: entrada_salida_03
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener contenido en la caja de texto y luego 
mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        '''
        nombre = self.txt_nombre.get()
        #apellido="De Paula Salles"
        #sector="RRHH"
        saludo= "hola" + nombre
        #otra forma de escribir un mensaje
        #saludo= "hola {0} {1}, trabajas en {2}".format(nombre,apellido,sector)
        alert(title= "Saludo", message= saludo)
        '''
        nombre= self.txt_nombre.get()
        saludo= "Buenos dias " + nombre
        alert(title= "EJ 03", message= saludo)

                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()