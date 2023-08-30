
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''

nombre: Mayra
apellido: De Paula Salles


Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en el vector lista_datos utilizando Dialog Alert para informar cada elemento.


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        #self.lista_datos = [2,3,5,7,11,13]
        

    def btn_mostrar_on_click(self):
        
        lista_datos= [2,3,5,7,11,13]
        for numero in lista_datos:

            alert(title= "LIST 01", message= numero)
        
        
'''
'''
Reclutando IT" Un recruiter nos contrató para armale un programa para el ingreso indeterminado de candidatos. Se solicitan los siguientes datos:   
nombre,
edad,   
sexo(feminino, masculino, no binario)
lenguaje( “Python”, “C#” o “Javascript”),
donde aprendió a programar(“universitario”,”terciario”,“curso”). 
LAS VALIDACIONES SON A CRITERIO DEL PROGRAMADOR
Informar:
a)El promedio de edad de los que estudian Python.
b)La cantidad de mujeres que estudian C#
c)El promedio de personas que aprendieron a programar en la Universidad.
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
        self.lista_edad = [25,35,28,24,30,32]
        self.lista_genero = ["femenino","masculino","no binario","masculino","femenino","femenino"]
        self.lista_lenguaje = ["Python","JS","C#","Python","C#","C#"]
        self.lista_instituto = ["universitario","curso","curso","terciario","universitario","curso"]


    def btn_cargar_on_click(self):
        respuesta_prompt= "si"

        while(respuesta_prompt != None):
           
            nombre_reclutado= prompt(title= "IT", prompt= "Ingrese su nombre")
            while (nombre_reclutado == None):
                nombre_reclutado= prompt(title= "IT", prompt= "Error, ingrese su nombre")
            self.lista_nombre.append(nombre_reclutado)

            edad_reclutado= prompt(title= "IT", prompt= "Ingrese su edad")
            while (edad_reclutado == None or int(edad_reclutado) < 18):
              edad_reclutado= prompt(title= "IT", prompt= "Error, ingrese su edad")
            edad_reclutado= int(edad_reclutado)
            self.lista_edad.append(edad_reclutado)

            genero_reclutado = prompt(title="IT", prompt="Ingrese Género: femenino, masculino, no binario")
            while (genero_reclutado == None or (genero_reclutado != "femenino" and genero_reclutado != "masculino" and genero_reclutado != "no binario")): #se usa AND y no OR
                genero_reclutado = prompt(title="IT", prompt="Error, ingrese Género válido: femenino, masculino, no binario")
            self.lista_genero.append(genero_reclutado)
            
            tipo_lenguaje_reclutado= prompt(title= "IT", prompt= "Ingrese su tipo de lenguaje: Python,C#,JS")
            while (tipo_lenguaje_reclutado == None or (tipo_lenguaje_reclutado != "Python" and tipo_lenguaje_reclutado != "C#" and tipo_lenguaje_reclutado != "JS")):
                tipo_lenguaje_reclutado= prompt(title= "IT", prompt= "Error, ingrese su tipo de lenguaje: Python,C#,JS")
            self.lista_lenguaje.append(tipo_lenguaje_reclutado)

            instituto_reclutado= prompt(title= "IT", prompt= "Ingrese su instituto: universitario,terciario,curso")
            while (instituto_reclutado == None or (instituto_reclutado != "universitario" and instituto_reclutado != "terciario" and instituto_reclutado != "curso")):
                instituto_reclutado= prompt(title= "IT", prompt= "Error, ingrese su tipo de elemento: universitario,terciario,curso")
            self.lista_instituto.append(instituto_reclutado)

            respuesta_prompt= prompt("Simulacro", "¿Desea continuar?")
    
    
    
    
    def btn_mostrar_on_click(self):
        # a)El promedio de edad de los que estudian Python.
        acumulador_edad= 0
        contador_edad= 0
        for i in range(len(self.lista_nombre)):
            if (self.lista_lenguaje[i] == "Python"):
                acumulador_edad= acumulador_edad + self.lista_edad[i]
                contador_edad= contador_edad + 1
        
        promedio_edad_python= acumulador_edad / contador_edad

        mensaje_1= f"El promedio de edad de los que estudian Python es: {promedio_edad_python}"
        #print(mensaje_1)


        # b)La cantidad de mujeres que estudian C#
        contador_mujeres_c= 0
        for i in range(len(self.lista_nombre)):
            match (self.lista_lenguaje[i]):
                case "C#":
                    if (self.lista_genero[i] == "femenino"):
                        contador_mujeres_c= contador_mujeres_c + 1

        mensaje_2= f"La cantidad de mujeres que estudian C# es: {contador_mujeres_c}"
        #print(mensaje_2)

        # c)El promedio de personas que aprendieron a programar en la Universidad.
        acumulador_personas_uni= 0
        contador_personas_uni= 0
        for i in range(len(self.lista_nombre)):
            if (self.lista_instituto[i] == "universitario"):
                acumulador_personas_uni= acumulador_personas_uni + self.lista_edad[i]
                contador_personas_uni= contador_personas_uni + 1

        promedio_personas_uni= acumulador_personas_uni / contador_personas_uni

        mensaje_3= f"El promedio de personas que aprendieron a programar en la Universidad es: {promedio_personas_uni}"
        print(mensaje_3) 
        

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()