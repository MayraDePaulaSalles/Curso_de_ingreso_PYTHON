'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


nombre: Mayra
apellido: De Paula Salles
---
Ejercicio: instrucion_if_01
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener contenido en la caja de texto txt_edad,
transformarlo en número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
     #2 valores posibles: True / False
     edad= self.txt_edad.get() 
     edad_numero= int(edad)

     if edad_numero == 18:
       
      alert(title="Respuesta", message= "Usted tiene 18 años") 
      
     
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
'''

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import tkinter as tk

'''
nombre: Mayra
apellido: De Paula Salles
'''

class App(customtkinter.CTk):
   
    def __init__(self):
        super().__init__()


        self.title("UTN FRA")
        self.minsize(320, 250)


        self.label_title = customtkinter.CTkLabel(master=self, text="Tour 🚂", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
   
    def btn_mostrar_on_click(self):
        # Se deben pedir los siguientes datos de un tour  de vacaciones a un destino en particular:

        # 1 -nombre , edad y género de una persona, mostrar el mensaje , "usted es  xxxx tiene xx de edad y su género es xxx"
        # 2 -pedir la altura de la persona e informar si es bajo: menor a 140 cm, medio entre 140 y 170 cm , alto hasta 190 cm y muy alto para mayores a esa altura.
        # 3- Validar todos los datos.
        # 4- En las vacaciones se pueden seleccionar distintas excursiones para realizar. Se pueden hacer desde 0 excursiones a 11 excursiones.
        # 5- Una vez ingresada la cantidad se debe pedir por cada excursión el importe y el tipo de excursión (caminata  o vehículo).
        # informar cual es el precio más caro, el más barato y el promedio.
        # 6- Informar cual es el tipo de excursión (caminata  o vehículo) más seleccionada o si se seleccionó las mismas veces (caminata  o vehículo)
        '''
        nombre= prompt(title= "EJ Tour", prompt= "Ingrese un su nombre")
        while nombre != str or nombre == None:
            nombre= prompt(title= "EJ Tour", prompt= "Error, ingrese un su nombre")
        
        edad= int(prompt(title= "EJ Tour", prompt= "Ingrese su edad"))
        while edad != int or edad < 0:
            edad= int(prompt(title= "EJ Tour", prompt= "Error, ingrese su edad"))
        
        genero= prompt(title= "EJ Tour", prompt= "Ingrese su genero: F, M, NB")
        while genero != str or (genero != "F" and genero != "M" and genero != "NB"):
            genero= prompt(title= "EJ Tour", prompt= "Error, ingrese su genero: F, M, NB")
        
        altura= int(prompt(title= "EJ Tour", prompt= "Ingrese su altura"))
        while altura != int:
            altura= int(prompt(title= "EJ Tour", prompt= "Error, ingrese su altura"))
        '''
        '''
        mensaje= "usted es  {0} tiene {1} de edad y su género es {2}".format(nombre,edad,genero)
        #alert(title= "EJ Tour", message= mensaje)

        if altura < 140:
            mensaje= "Es bajo"
        elif altura <= 170:
            mensaje= "Es medio"
        elif altura <= 190:
            mensaje= "Es alto"
        else:
            mensaje="Es muy alto"

        alert(title= "EJ Tour", message= mensaje)
        '''




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()





