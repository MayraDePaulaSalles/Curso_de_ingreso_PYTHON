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
        '''
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
        '''
        '''
        Cada televidente que vota deberá ingresar:
        Nombre del votante
        Edad del votante (debe ser mayor a 13)
        Género del votante (Masculino, Femenino, Otro)
        El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
        No se sabe cuántos votos entrarán durante la gala.
        Se debe informar al usuario:
        A- El promedio de edad de las votantes de género Femenino 
        B- Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
        C- Nombre del votante más joven qué votó a Gianni.
        D- Nombre de cada participante y porcentaje de los votos qué recibió.
        E- El nombre del participante que debe dejar la casa (El que tiene más votos)
        '''
        respuesta_prompt= "si"
        acumulador_edad_fem= 0
        contador_edad_fem= 0
        contador_voto_masculino= 0
        bandera_primero= True
        nombre_votante_joven= "" 
        contador_giovanni= 0
        contador_facundo= 0
        contador_gianni= 0
        

        
        while (respuesta_prompt != None):
            
            nombre= prompt(title= "Gran Uteniano", prompt= "Ingrese su nombre")
            while (not nombre.isalpha() or nombre == None):
                nombre= prompt(title= "Gran Uteniano", prompt= "Error, ingrese su nombre")
            
            edad= prompt(title= "Gran Uteniano", prompt= "Ingrese su edad")
            while (not edad.isdigit() or edad == None):
              edad= prompt(title= "Gran Uteniano", prompt= "Error, ingrese su edad") 
            edad= int(edad)
            
            genero= prompt(title= "Gran Uteniano", prompt= "Ingrese su genero: Femenino, Masculino, Otro")
            while (not genero.isalpha() or (genero != "Femenino" and genero != "Masculino" and genero != "Otro") or genero == None):
                genero= prompt(title= "Gran Uteniano", prompt= "Error, ingrese su genero: Femenino, Masculino, Otro")    
  
            participante_voto_negativo= prompt(title= "Gran Uteniano", prompt= "Ingrese el nombre del participante con su voto negativo: Giovanni, Facundo, Gianni")
            while ((participante_voto_negativo != "Giovanni" and participante_voto_negativo != "Facundo" and participante_voto_negativo != "Gianni") or not participante_voto_negativo.isalpha() or participante_voto_negativo == None):
                 participante_voto_negativo= prompt(title= "Gran Uteniano", prompt= "Error, ingrese el nombre del participante con su voto negativo")
            '''        
            match (genero):
                case "Femenino":
                    contador_edad_fem= contador_edad_fem + 1
                    acumulador_edad_fem= acumulador_edad_fem + edad

                    promedio_edad= acumulador_edad_fem / contador_edad_fem
            
                case "Masculino":
                    if (edad >= 25 and edad <= 40 and participante_voto_negativo == "Giovanni" or participante_voto_negativo == "Facundo"):
                            contador_voto_masculino= contador_voto_masculino + 1
            
            match participante_voto_negativo:
                case "Gianni":
                    if (bandera_primero == True):
                        edad_votante_joven= edad
                        edad_votante_grande= edad
                        bandera_primero = False
                    else:
                        if (edad < edad_votante_joven):
                            edad_votante_joven = edad
                            nombre_votante_joven= nombre
                        
                        elif (edad > edad_votante_grande):
                            edad_votante_grande = edad

            '''
           
            if (participante_voto_negativo == "Giovanni"):
                contador_giovanni= contador_giovanni + 1 
            
            elif(participante_voto_negativo == "Facundo"):
                contador_facundo= contador_facundo + 1

            elif(participante_voto_negativo == "Gianni"):
                contador_gianni= contador_gianni + 1

            porcentaje_votos_giovanni= contador_giovanni * participante_voto_negativo / 100
            porcentaje_votos_facundo= contador_facundo * participante_voto_negativo / 100
            porcentaje_votos_gianni= contador_gianni * participante_voto_negativo / 100

            informe= f"Giovanni saco un {porcentaje_votos_giovanni}\n\
            Facundo saco un {porcentaje_votos_facundo}\n\
            Gianni saco un {porcentaje_votos_gianni}"


            respuesta_prompt= prompt("Gran Uteniano", "¿Desea continuar?")
            
            print(informe)
            '''
            informe= f"El promedio de edad de las votantes de género Femenino es:{promedio_edad}\n\
            la cantidad de personas de género masculino que votaron por Giovanni o Facundo es:{contador_voto_masculino}\n\
            nombre del votante más joven qué votó a Gianni es:{nombre_votante_joven}" 
            #alert("Gran Uteniano", contador_voto_masculino)
            '''
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
