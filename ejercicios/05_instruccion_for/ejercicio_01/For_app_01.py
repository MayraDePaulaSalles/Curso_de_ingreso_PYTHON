import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre: Mayra
apellido: De Paula Salles

Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        for i in range(1,6,1): # inicio,fin excluyente, salto
            alert(title="FOR 01", message= i)
       
-------------------------------------------------------------------------------------------  
Inmoviliaria: Nos piden armar un programa para ingresar los siguientes datos de los inquilinos de los inmuebles: 
nombre,
lugar(CABA, Conurbano, Interior) 
tipo( dpto, casa, quinta) en CABA solo se alquilan dptos y casas
cantidad de habitantes (1-3 p/ dpto, 1-7 p/casa, 1-15 p/ quinta)
alquiler
INFORMAR: 
a) Cantidad de casa alquiladas en CABA
b) El inquilino con alquiler más caro
c) Del interior del país, la quinta más cara
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        #self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        #self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = ["Maria","Jose","Juan","Matias","Laura","Liz"]
        self.lista_lugar = ["CABA","Conurbano","Interior","CABA","CABA","Conurbano"]
        self.lista_tipo = ["dpto","casa","quinta","casa","dpto","quinta"]
        self.lista_cantidad_habitantes= [2,5,12,4,3,10]
        self.lista_alquiler= [150,260,380,230,200,360]


    def btn_cargar_on_click(self): 
        respuesta_prompt= "si"

        while(respuesta_prompt != None):
           
            nombre_ingresado= prompt(title= "Inmoviliaria", prompt= "Ingrese su nombre")
            while (nombre_ingresado == None):
                nombre_ingresado= prompt(title= "Inmoviliaria", prompt= "Error, ingrese su nombre")
            self.lista_nombre.append(nombre_ingresado)

            lugar_ingresado = prompt(title="Inmoviliaria", prompt="Ingrese lugar: CABA, Conurbano, Interior")
            while (lugar_ingresado == None or (lugar_ingresado != "CABA" and lugar_ingresado != "Conurbano" and lugar_ingresado != "Interior")): #se usa AND y no OR
                lugar_ingresado = prompt(title="Inmoviliaria", prompt="Error, ingrese lugar válido: CABA, Conurbano, Interior")
            self.lista_lugar.append(lugar_ingresado)

            tipo_lugar_ingresado = prompt(title="Inmoviliaria", prompt="Ingrese tipo de lugar: dpto, casa, quinta")
            while (tipo_lugar_ingresado == None or (tipo_lugar_ingresado != "dpto" and tipo_lugar_ingresado != "casa" and tipo_lugar_ingresado != "quinta")): #se usa AND y no OR
                tipo_lugar_ingresado = prompt(title="Inmoviliaria", prompt="Error, ingrese tipo de lugar: dpto, casa, quinta")
            self.lista_tipo.append(tipo_lugar_ingresado)

            cantidad_habitantes_ingresada= prompt(title= "Inmoviliaria", prompt= "Ingrese cantidad de habitantes: (1-3 p/ dpto, 1-7 p/casa, 1-15 p/ quinta)")
            while (cantidad_habitantes_ingresada == None or (int(cantidad_habitantes_ingresada) < 1 or int(cantidad_habitantes_ingresada) > 15)):
                cantidad_habitantes_ingresada= prompt(title= "Inmoviliaria", prompt= "Error, ingrese cantidad de habitantes: (1-3 p/ dpto, 1-7 p/casa, 1-15 p/ quinta)")
            cantidad_habitantes_ingresada= int(cantidad_habitantes_ingresada)
            self.lista_cantidad_habitantes.append(cantidad_habitantes_ingresada)

            alquiler_ingresado= prompt(title= "Inmoviliaria", prompt= "Ingrese su alquiler:")
            while (alquiler_ingresado == None or int(alquiler_ingresado) < 0):
              alquiler_ingresado= prompt(title= "Inmoviliaria", prompt= "Error, ingrese su alquiler")
            alquiler_ingresado= int(alquiler_ingresado)
            self.lista_alquiler.append(alquiler_ingresado)


            respuesta_prompt= prompt("Simulacro", "¿Desea continuar?")
    
    
    
    def btn_mostrar_on_click(self):
        # a) Cantidad de casas alquiladas en CABA
        contador_casas_alquiladas= 0
        for i in range(len(self.lista_lugar)):
            if (self.lista_lugar[i] == "CABA"):
                    match (self.lista_tipo[i]):
                        case "casa":
                            contador_casas_alquiladas= contador_casas_alquiladas + 1

        mensaje_1= f"Cantidad de casas alquiladas en CABA: {contador_casas_alquiladas}"
        #print(mensaje_1)


        #b) El inquilino con alquiler más caro
        bandera_primero= True
        lista_nombre= self.lista_nombre
        lista_alquiler= self.lista_alquiler

        for i in range(len(self.lista_nombre)):
            if (bandera_primero == True):
                alquiler_mas_caro = lista_alquiler[0]
                inquilino_mas_caro = lista_nombre[0] 
                bandera_primero = False
            else:
                if (lista_alquiler[i] > alquiler_mas_caro):
                    alquiler_mas_caro = lista_alquiler[i]
                    inquilino_mas_caro = lista_nombre[i]

        mensaje_2= f"El inquilino con alquiler más caro es: {inquilino_mas_caro}"
        #print(mensaje_2)


        #c) Del interior del país, la quinta más cara
        bandera_primero= True
        lista_alquiler= self.lista_alquiler
        for i in range(len(self.lista_lugar)):
            if(self.lista_lugar[i] == "Interior"):
                if (self.lista_tipo[i] == "quinta"):
                    if (bandera_primero == True):
                        quinta_mas_cara = lista_alquiler[0]
                        bandera_primero = False
                    else:
                        if (lista_alquiler[i] > quinta_mas_cara):
                            quinta_mas_cara = lista_alquiler[i]

        mensaje_3= f"Del interior del país, la quinta más cara es:{quinta_mas_cara}"
        print(mensaje_3)


          

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()