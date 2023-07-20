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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativos= 0
        acumulador_positivos= 0
        contador_positivos= 0
        contador_negativos= 0
        contador_ceros= 0


        while (True):
            numero= prompt("EJ 10", "Ingrese los numeros que quiera")
            
            
            if (numero == None or numero == ""):
                break
            
            numero= float(numero)
            if (numero < 0):
                acumulador_negativos= acumulador_negativos + numero
                contador_negativos= contador_negativos + 1
                
            elif (numero > 0):
                acumulador_positivos= acumulador_positivos + numero
                contador_positivos= contador_positivos + 1
        
            else:
                contador_ceros= contador_ceros + 1
                

            resta_numeros= contador_positivos - contador_negativos
            
            mensaje= "Suma negativos: {0}, Cantidad negativos: {1}, Suma  positivos: {2}, Cantidad  positivos: {3}, Cantidad ceros: {4}, Resta cantidad positivos y negativos: {5} ".format(acumulador_negativos,contador_negativos,acumulador_positivos,contador_positivos,contador_ceros,resta_numeros)
        
            
        
        alert(title= "EJ 10", message= mensaje)
            

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
