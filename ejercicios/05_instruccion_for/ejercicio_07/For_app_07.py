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
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_impares= 0
        numero= prompt(title= "FOR 07", prompt= "Ingrese un numero")
        numero= int(numero)
        for i in range(1,numero + 1,1):
            if(i % 2 == 1 ):
                contador_impares= contador_impares + 1
                alert (title= "FOR 07", message= i)
        
        alert(title= "FOR 07", message= f"Cantidad de numeros pares econtrados:{contador_impares}")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()