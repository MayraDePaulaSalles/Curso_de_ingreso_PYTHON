import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Mayra
apellido: De Paula Salles
'''
'''
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        numero= 0
        while (numero < 10): #de esta forma se excluye el numero maximo o limite
            numero= numero + 1
            alert(title= "EJ 01", message= str(numero))

        """
        numero= 1 #inicializacion de mi variable de control
        while (numero <= 10): #condicion para controlar cuantas veces se debe iterar
            alert(message= str(numero))
            numero= numero + 1 #le sumo 1
            
            #sali del while

            #validaciones para mas adelante
            while  numero == None or numero.isdigit() == False or int(numero) < 0 or int(numero) > 9:
            numero = prompt(title="UTN",prompt="ingrese un numero del 0 al 9")
        """
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()