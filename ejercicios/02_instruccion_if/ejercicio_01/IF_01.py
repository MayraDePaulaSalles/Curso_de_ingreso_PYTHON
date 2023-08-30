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
        
        respuesta_prompt= "si"
        contador_excursiones= 0
        bandera_primero= True
        tipo_mas_caro= ""
        tipo_mas_barato= ""
        tipo_mas_seleccionado= ""
        suma_excursiones= 0
        cont_tipo_seleccionado= 0
       
        while (respuesta_prompt != None):
            
            nombre= prompt(title= "EJ Tour", prompt= "Ingrese su nombre")
            while (not nombre.isalpha() or nombre == None):
                nombre= prompt(title= "EJ Tour", prompt= "Error, ingrese su nombre")

            edad= prompt(title= "EJ Tour", prompt= "Ingrese su edad")
            while (not edad.isdigit() or edad == None):
              edad= prompt(title= "EJ Tour", prompt= "Error, ingrese su edad")
            edad= int(edad)
            
            genero= prompt(title= "EJ Tour", prompt= "Ingrese su genero: F, M, NB")
            while (not genero.isalpha() or (genero != "F" and genero != "M" and genero != "NB")or genero == None):
                genero= prompt(title= "EJ Tour", prompt= "Error, ingrese su genero: F, M, NB")
            
            altura= prompt(title= "EJ Tour", prompt= "Ingrese su altura")
            while (not altura.isdigit() or altura == None):
                altura= prompt(title= "EJ Tour", prompt= "Error, ingrese su altura")
                
            altura= int(altura)
            if altura < 140:
                mensaje_dos= "es bajo/a"
            elif altura <= 170:
                mensaje_dos= "es medio alto/a"
            elif altura <= 190:
                mensaje_dos= "es alto/a"
            else:
                mensaje_dos= "es muy alto/a"
            
            
            informe= "Usted es {0}, tiene {1} años de edad, su género es {2} y de altura mide {3},{4}".format(nombre,edad,genero,altura,mensaje_dos)
                      
            
            cant_excursiones= prompt(title="EJ Tour", prompt= "Ingrese la cantidad de excursiones que realizara")
            while (not cant_excursiones.isdigit() or cant_excursiones == None):
              cant_excursiones= prompt(title= "EJ Tour", prompt= "Error, ingrese la cantidad de excursiones que realizara")
            
            cant_excursiones= int(cant_excursiones)

            while (contador_excursiones < cant_excursiones):
                
                importe= prompt(title= "EJ Tour", prompt= "Ingrese su importe") 
                while (not importe.isdigit() or importe == None):
                    importe= prompt(title= "EJ Tour", prompt= "Error, ingrese su importe")
                
                importe= int(importe)
           
                tipo_excursion= prompt(title= "EJ Tour", prompt= "Ingrese el tipo de excursion: caminata o vehiculo")
                while (not tipo_excursion.isalpha() or (tipo_excursion != "caminata" and tipo_excursion != "vehiculo") or tipo_excursion == None):
                    tipo_excursion= prompt(title= "EJ Tour", prompt= "Error, ingrse tipo de excursion: caminata o vehiculo")

                if (bandera_primero == True):
                    precio_mas_caro= importe
                    precio_mas_barato= importe
                    tipo_mas_caro= tipo_excursion
                    tipo_mas_barato= tipo_excursion
                    tipo_mas_seleccionado= tipo_excursion
                    bandera_primero = False 
                else:
                    if (importe > precio_mas_caro):
                        precio_mas_caro = importe
                        tipo_mas_caro = tipo_excursion

                    elif (importe < precio_mas_barato):
                        precio_mas_barato = importe
                        tipo_mas_barato = tipo_excursion

                    elif (tipo_excursion > tipo_mas_seleccionado):
                        tipo_mas_seleccionado = tipo_excursion

                #if (tipo_mas_seleccionado == "caminata" and tipo_mas_seleccionado == "vehiculo"):
                         
                
                suma_excursiones= suma_excursiones + importe
                contador_excursiones= contador_excursiones + 1
                cont_tipo_seleccionado= cont_tipo_seleccionado + 1
                
            promedio_importe= suma_excursiones / cant_excursiones

            informe= f"La excursion mas cara vale ${precio_mas_caro} y es de {tipo_mas_caro}\n\
                La excursion mas barata vale ${precio_mas_barato} y es de {tipo_mas_barato}\n\
                El tipo de excusion mas seleccionado fue:{tipo_mas_seleccionado}\n\
                El promedio de precios de las excursiones es de ${promedio_importe}"
            
            
            respuesta_prompt= prompt(title= "TP TOUR", prompt= "¿Desea continuar?")
            
            alert(title= "EJ Tour", message= informe)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()





