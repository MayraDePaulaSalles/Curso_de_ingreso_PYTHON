import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mayra 
apellido: De Paula Salles
---
Ejercicio: entrada_salida_04
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt 
y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
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
        #ingreso el nombre por prompt y lo guardo en la variable nombre
        nombre = prompt(title= "Ej 4", prompt= "Ingrese su nombre")
        #aca pongo el nombre en la caja de texto
        self.txt_nombre.delete(0,1000) #vacia la caja para ingresar un dato nuevo
        self.txt_nombre.insert(0, nombre) #inserta un dato
        '''
        nombre= prompt(title="Pregunta", prompt="¿Cual es su nombre?")
        self.txt_nombre.delete(0,10000)
        self.txt_nombre.insert(0,nombre)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()