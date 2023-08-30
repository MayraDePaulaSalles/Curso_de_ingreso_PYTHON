'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)
'''
'''
nombre: Mayra
apellido: De Paula Salles
'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        respuesta_prompt= "si"
        bandera_primero= True
        acumulador_edades= 0
        contador_edades= 0
        total_votos= 0 

        while (respuesta_prompt != None):

            nombre= prompt(title= "TP 06", prompt= "Ingrese su nombre")
            while (not nombre.isalpha() or nombre == None):
                nombre= prompt(title= "TP 06", prompt= "Error, ingrese su nombre")

            edad= prompt(title= "TP 06", prompt= "Ingrese su edad")
            while (edad == None or int(edad) < 25):
              edad= prompt(title= "TP 06", prompt= "Error, ingrese su edad")
            edad= int(edad)

            cantidad_votos= prompt(title= "TP 06", prompt= "Ingrese la cantidad de votos")
            while (cantidad_votos == None or int(cantidad_votos) < 0):
              cantidad_votos= prompt(title= "TP 06", prompt= "Error, ingrese la cantidad de votos")
            cantidad_votos= int(cantidad_votos)

            


            if (bandera_primero == True):
                candidato_mas_votos = cantidad_votos
                candidato_menos_votos = cantidad_votos
                nombre_mas_votos= nombre
                nombre_menos_votos = nombre
                edad_menos_votos = edad
                bandera_primero = False
            else:
                if (cantidad_votos > candidato_mas_votos):
                    candidato_mas_votos = cantidad_votos
                    nombre_mas_votos = nombre
                
                elif (cantidad_votos < candidato_menos_votos):
                    candidato_menos_votos = cantidad_votos
                    nombre_menos_votos = nombre
                    edad_menos_votos = edad

            total_votos= total_votos + cantidad_votos
            
            contador_edades= contador_edades + 1
            acumulador_edades= acumulador_edades + edad
            
            respuesta_prompt= prompt(title= "TP 06", prompt= "¿Desea continuar?")
  
        promedio_edades= acumulador_edades / contador_edades

        informe= f"nombre del candidato con más votos:{nombre_mas_votos}\n\
        nombre y edad del candidato con menos votos:{nombre_menos_votos},{edad_menos_votos}años\n\
        el promedio de edades de los candidatos:{promedio_edades}\n\
        total de votos emitidos:{total_votos}"
        
        print(informe)


                

'''
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre (validar que no sea None), la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Pedir Datos", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Datos", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=6, pady=20, columnspan=2, sticky="nsew")
        self.lista_de_nombres = ['Pelusa', 'Freya', 'Sirius', 'Pepe Peposo', 'Hooper'] 
        self.lista_de_edades = [33, 28, 29, 26, 42] 
        self.lista_de_votos_por_candidato = [120, 9, 20, 1090, 2491]
        
    def btn_validar_on_click(self):
        respuesta_prompt= "si"

        while(respuesta_prompt != None):
            
            nombre_ingresado= prompt(title= "TP 06", prompt= "Ingrese su nombre")
            while (nombre_ingresado == None):
                nombre_ingresado= prompt(title= "TP 06", prompt= "Error, ingrese su nombre")
            self.lista_de_nombres.append(nombre_ingresado)

            edad_ingresada= prompt(title= "TP 06", prompt= "Ingrese su edad")
            while (edad_ingresada == None or int(edad_ingresada) < 25):
              edad_ingresada= prompt(title= "TP 06", prompt= "Error, ingrese su edad")
            edad_ingresada= int(edad_ingresada)
            self.lista_de_edades.append(edad_ingresada)

            cantidad_votos_ingresada= prompt(title= "TP 06", prompt= "Ingrese la cantidad de votos")
            while (cantidad_votos_ingresada == None or int(cantidad_votos_ingresada) < 0):
              cantidad_votos_ingresada= prompt(title= "TP 06", prompt= "Error, ingrese la cantidad de votos")
            cantidad_votos_ingresada= int(cantidad_votos_ingresada)
            self.lista_de_votos_por_candidato.append(cantidad_votos_ingresada)

            
            respuesta_prompt= prompt("TP 05", "¿Desea continuar?")


    def btn_mostrar_on_click(self):
        

        # a. nombre del candidato con más votos
        largo= len(self.lista_de_votos_por_candidato)
        mayor_cantidad_votos= None
        nombre_candidato_mas_votos= "" 
        menor_cantidad_votos= None
        nombre_candidato_menos_votos= ""
        edad_candidato_menos_votos= 0
        acumulador_edad_candidatos= 0
        suma_votos_emitidos= 0
        

        for i in range(largo): 
            if (mayor_cantidad_votos == None or  mayor_cantidad_votos < self.lista_de_votos_por_candidato[i]):
                mayor_cantidad_votos = self.lista_de_votos_por_candidato[i]
                nombre_candidato_mas_votos = self.lista_de_nombres[i]
        # b. nombre y edad del candidato con menos votos 
            if(menor_cantidad_votos == None or menor_cantidad_votos > self.lista_de_votos_por_candidato[i]):
                menor_cantidad_votos = self.lista_de_votos_por_candidato[i]  
                nombre_candidato_menos_votos = self.lista_de_nombres[i]
                edad_candidato_menos_votos = self.lista_de_edades[i]
        # c. el promedio de edades de los candidatos 
            acumulador_edad_candidatos = acumulador_edad_candidatos + self.lista_de_edades[i]

        promedio_edad_candidatos= acumulador_edad_candidatos / largo
        # d. total de votos emitidos
        suma_votos_emitidos= suma_votos_emitidos + self.lista_de_votos_por_candidato[i]

        mensaje= f"El nombre del candidato con mas votos es:{nombre_candidato_mas_votos}.\n\
        El nombre y edad del candidato con menos votos es:{nombre_candidato_menos_votos} de {edad_candidato_menos_votos}\n\
        El promedio de edades de los candidatos es{promedio_edad_candidatos}\n\
        El total de votos emitidos es{suma_votos_emitidos}"
        print(mensaje)

        

        largo_lista= len(self.lista_de_votos_por_candidato)
        lista_votos_candidatos= self.lista_de_votos_por_candidato
        lista_nombres_candidatos= self.lista_de_nombres 
        lista_edad_candidatos= self.lista_de_edades
        flag= True
        suma_edad_candidatos= 0
        suma_total_votos= 0
        largo_lista_edad= len(self.lista_de_edades)
        
        
        if (flag == True):
            maximo = lista_votos_candidatos[0]
            minimo = lista_votos_candidatos[0]
            max_nombre = lista_nombres_candidatos[0]
            min_nombre = lista_nombres_candidatos[0]
            min_edad = lista_edad_candidatos[0]
            flag = False
        # a. nombre del candidato con más votos
        for i in range(largo_lista):
            if (lista_votos_candidatos[i] > maximo):
                maximo = lista_votos_candidatos[i]
                max_nombre = lista_nombres_candidatos[i]
        # b. nombre y edad del candidato con menos votos
            elif (lista_votos_candidatos[i] < minimo):
                minimo = lista_votos_candidatos[i]
                min_nombre = lista_nombres_candidatos[i]
                min_edad = lista_edad_candidatos[i]

        # c. el promedio de edades de los candidatos

            suma_edad_candidatos= suma_edad_candidatos + lista_edad_candidatos[i]

            
        # d. total de votos emitidos
            suma_total_votos= suma_total_votos + lista_votos_candidatos[i]

        promedio_edad_candidatos= suma_edad_candidatos / largo_lista_edad


        mensaje= f"El nombre del candidato con mas votos es:{max_nombre}.\n\
        El nombre y edad del candidato con menos votos es:{min_nombre} de {min_edad}\n\
        El promedio de edades de los candidatos es:{promedio_edad_candidatos}\n\
        El total de votos emitidos es:{suma_total_votos}"
        print(mensaje)
'''        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
