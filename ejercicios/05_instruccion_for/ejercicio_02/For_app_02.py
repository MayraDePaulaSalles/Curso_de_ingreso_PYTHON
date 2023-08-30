import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre: Mayra
apellido: De Paula Salles
'''
'''
Enunciado del parcial:
Una distribuidora de bebidas llena 10 comiones con sus productos y necesita guardar ciertos datos de cada una:
-Nombre del conductor
-Cantidad de litros de agua transportada($300 el litro)
-Cantidad de litros de gaseosa transportada ($600 el litro)
-Cantidad de litros de cerveza transportada ($800 el litro)
-Cantidad de litros de vino transportada ($1000 el litro)

Obligatorio: Informar el promedio de litros por camion.

Por  terminación de DNI:
deberá realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
   
    1- Tome el último número de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el último número de su DNI Personal (Ej 4), y restarle al número 9 (Ej 9-4 = 5).
    Realiza el informe correspondiente al número obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR.

0)Debemos mostrar que tipo de bebida se transportó en mayor cantidad (cerveza, agua, gaseosa o vino).
1)Debemos mostrar el total de facturación del agua y la gaseosa vendida que estará dado por cada litro de gaseosa $600 y cada litro de agua a $300.
2)Debemos mostrar el total de facturación de la cerveza y el vino vendido que estará dado por cada litro de cerveza $800 y cada litro de vino a $1000.
3)Si la empresa supera la facturación de 350000 pesos deberá pagar un 8% de ingresos brutos. Informar si lo paga y de ser así el monto del impuesto.
4)Si la empresa supera la facturación de 700000 pesos deberá pagar un 15% de impuesto a las ganancias. Informar si lo paga y de ser así el monto del impuesto.
5)Debemos mostrar que tipo de bebida se transportó en menor cantidad (cerveza, agua, gaseosa o vino).
6)Informar el porcentaje de agua transportada y de gaseosa transportada en relación al total de litros transportados.
7)Informar el porcentaje de cerveza transportada y de vino transportado en relación al total de litros transportados.
8)Informar el primer ingreso (camion) que transporte mas de 100 litros.
9)Informar el primer ingreso (camion) que transporte menos de 50 litros.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Simulacro Parcial")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre = ["Jose","Juan","Pedro"] #,"Carlos","Mario","Leo","Dante","Mauro","Tomas","Raul"
        self.lista_cantidad_litros_agua = [60,45,40]
        self.lista_cantidad_litros_gaseosa = [50,45,30]
        self.lista_cantidad_litros_cerveza = [40,25,30]
        self.lista_cantidad_litros_vino = [30,25,30]


    def btn_cargar_on_click(self):
        respuesta_prompt= "si"

        while(respuesta_prompt != None):
           
            nombre_ingresado= prompt(title= "Parcial", prompt= "Ingrese su nombre")
            while (nombre_ingresado == None):
                nombre_ingresado= prompt(title= "Parcial", prompt= "Error, ingrese su nombre")
            self.lista_nombre.append(nombre_ingresado)

            cantidad_litros_agua= prompt(title= "Parcial", prompt= "Ingrese cantidad de litros de agua transportanda")
            while (cantidad_litros_agua == None or (int(cantidad_litros_agua) < 0 or int(cantidad_litros_agua) > 100)):
                cantidad_litros_agua= prompt(title= "Parcial", prompt= "Error, ingrese cantidad litros de agua transportanda")
            cantidad_litros_agua= int(cantidad_litros_agua)
            self.lista_cantidad_litros_agua.append(cantidad_litros_agua)

            cantidad_litros_gaseosa= prompt(title= "Parcial", prompt= "Ingrese cantidad de litros de gaseosa transportada")
            while (cantidad_litros_gaseosa == None or (int(cantidad_litros_gaseosa) < 0 or int(cantidad_litros_gaseosa) > 100)):
                cantidad_litros_gaseosa= prompt(title= "Parcial", prompt= "Error, ingrese cantidad de litros de gaseosa transportada")
            cantidad_litros_gaseosa= int(cantidad_litros_gaseosa)
            self.lista_cantidad_litros_gaseosa.append(cantidad_litros_gaseosa)

            cantidad_litros_cerveza= prompt(title= "Parcial", prompt= "Ingrese cantidad de litros de cerveza transportada")
            while (cantidad_litros_cerveza == None or (int(cantidad_litros_cerveza) < 0 or int(cantidad_litros_cerveza) > 100)):
                cantidad_litros_cerveza= prompt(title= "Parcial", prompt= "Error, ingrese cantidad de litros de cerveza transportada")
            cantidad_litros_cerveza= int(cantidad_litros_cerveza)
            self.lista_cantidad_litros_cerveza.append(cantidad_litros_cerveza)

            cantidad_litros_vino= prompt(title= "Parcial", prompt= "Ingrese cantidad de litros de vino tranportada ")
            while (cantidad_litros_vino == None or (int(cantidad_litros_vino) < 0 or int(cantidad_litros_vino) > 100)):
                cantidad_litros_vino= prompt(title= "Parcial", prompt= "Error, ingrese cantidad de litros de vino tranportada")
            cantidad_litros_vino= int(cantidad_litros_vino)
            self.lista_cantidad_litros_vino.append(cantidad_litros_vino)

            respuesta_prompt= prompt("Pacial", "¿Desea continuar?")




    def btn_mostrar_on_click(self):
        #Obligatorio: Informar el promedio de litros por camion. 
        for i in range(len(self.lista_nombre)):
            total_litros= self.lista_cantidad_litros_agua[i] + self.lista_cantidad_litros_gaseosa[i] + self.lista_cantidad_litros_cerveza[i] + self.lista_cantidad_litros_vino[i]

            promedio_litros= total_litros / 4

            mensaje_1= f"el promedio de litros por camion {i+1} es: {promedio_litros}"
            print(mensaje_1)
            
    
    def btn_informar_on_click(self):
        #Realizar informe 2
        #2)Debemos mostrar el total de facturación de la cerveza y el vino vendido que estará dado por cada litro de cerveza $800 y cada litro de vino a $1000.
        suma_cerveza= 0
        suma_vino= 0
        litro_cerveza_precio= 800
        litro_vino_precio= 1000

        for i in range(len(self.lista_nombre)):
            
            suma_cerveza= suma_cerveza + self.lista_cantidad_litros_cerveza[i] 
        
            suma_vino= suma_vino + self.lista_cantidad_litros_vino[i]

        total_litro_cerveza= suma_cerveza * litro_cerveza_precio 
        total_litro_vino= suma_vino * litro_vino_precio      


        mensaje_2= f"El total de facturacion de cerveza : {total_litro_cerveza},y de vino es: {total_litro_vino}"
        print(mensaje_2)


        #7)Informar el porcentaje de cerveza transportada y de vino transportado en relación al total de litros transportados.
    
        
        for i in range(len(self.lista_nombre)):
             
            contador_litros_cerveza= len(self.lista_cantidad_litros_cerveza)
            contador_litros_vino= len(self.lista_cantidad_litros_vino)
        
        porcentaje_litros_cerveza= contador_litros_cerveza * 100 / 4   
        porcentaje_litros_vino= contador_litros_vino * 100 / 4

        mensaje_3= f"El porcentaje total de cerveza transportada es: {porcentaje_litros_cerveza}\nEl porcentaje total de vino transportado es: {porcentaje_litros_vino}"
        print(mensaje_3)
       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()