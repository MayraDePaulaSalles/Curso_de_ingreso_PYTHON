'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        
       #VALIDACIONES
        # lista_nombre = ["PATO","SELE","FABRI","CESAR","JESI","VIR","PEPE","PABLO"]
        # lista_edad = [26,27,33,24,35,28,30,40]
        # lista_genero = ["M","F","M","M","F","F","NB","NB"]
        # lista_tecnologia = ["PYTHON","PYTHON","PYTHON","JS","JS","JS","JS","ASP.NET"]
        # lista_puesto = ["Jr","Jr","Sr","Jr","Jr","Jr","Ssr","Ssr"]
        lista_nombre = []
        lista_edad = []
        lista_genero = []
        lista_tecnologia = []
        lista_puesto = []
        
        for i in range (1,11,1): #Definitivo es 11, probar con 4 al principio
            nombre = prompt(title="UTN", prompt="Ingrese un nombre")
            lista_nombre.append(nombre)
            
            edad = int(prompt(title="UTN", prompt="Ingrese una edad"))
            while edad < 18:
                edad = int(prompt(title="ERROR", prompt="Ingrese una edad válida"))
            lista_edad.append(edad)
            
            genero = prompt(title="UTN", prompt="Ingrese Género: F-M-NB")
            while genero != "F" and genero != "M" and genero != "NB": #se usa AND y no OR
                genero = prompt(title="ERROR", prompt="Ingrese Género válido: F-M-NB")
            lista_genero.append(genero)

            tecnologia = prompt(title="UTN", prompt="Ingrese Tecnologia: PYTHON-JS-ASP.NET")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                genero = prompt(title="ERROR", prompt="Ingrese Tecnología válida: PYTHON-JS-ASP.NET")
            lista_tecnologia.append(tecnologia)

            puesto = prompt(title="UTN", prompt="Ingrese Puesto: Jr-Ssr-Sr")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt(title="ERROR", prompt="Ingrese Puesto válido: Jr-Ssr-Sr")
            lista_puesto.append(puesto)

        #INFORMES
        largo_edad = len(lista_edad)
        cantidad_postulantes_A = 0
        nombre_postulante_jr_menor_edad = None
        menor_edad = None
        suma_edad_M = 0
        suma_edad_F = 0
        suma_edad_NB = 0
        contador_edad_M = 0
        contador_edad_F = 0
        contador_edad_NB = 0
        contador_PYTHON = 0
        contador_JS = 0
        contador_ASP_NET = 0

        for i in range(largo_edad):
            #A Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
            #cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
            if lista_edad[i] >= 25 and lista_edad[i] <= 40:
                match lista_genero[i]:
                    case "NB":
                        match lista_tecnologia[i]:
                            case "ASP.NET"|"JS":
                                match lista_puesto[i]:
                                    case "Ssr":
                                        cantidad_postulantes_A += 1                           
            #B Nombre del postulante Jr con menor edad.
            if (menor_edad == None and lista_puesto[i] == "Jr") or (lista_edad[i] < menor_edad and lista_puesto[i] == "Jr"):
                menor_edad = lista_edad[i]
                nombre_postulante_jr_menor_edad = lista_nombre[i]
            #C Promedio de edades por género.
            match lista_genero[i]:
                case "M":
                    suma_edad_M += lista_edad[i]
                    contador_edad_M += 1
                case "F":
                    suma_edad_F += lista_edad[i]
                    contador_edad_F += 1
                case "NB":
                    suma_edad_NB += lista_edad[i]
                    contador_edad_NB += 1
            #D Tecnologia con mas postulantes (solo hay una).
            if lista_tecnologia[i] == "PYTHON":
                contador_PYTHON += 1
            else:
                if lista_tecnologia[i] == "JS":
                    contador_JS += 1
                else:
                    contador_ASP_NET +=1
            if (contador_PYTHON > contador_JS) and (contador_PYTHON > contador_ASP_NET):
                tecnologia_con_mas_postulantes = "PYTHON"
            elif (contador_JS > contador_PYTHON) and (contador_JS > contador_ASP_NET):
                tecnologia_con_mas_postulantes = "JS"
            else:
                tecnologia_con_mas_postulantes = "ASP.NET"
            #E Porcentaje de postulantes de cada genero.
            if (contador_edad_M + contador_edad_F + contador_edad_NB) == largo_edad:
                porcentaje_M = contador_edad_M * 100 / (contador_edad_M + contador_edad_F + contador_edad_NB)
                porcentaje_F = contador_edad_F * 100 / (contador_edad_M + contador_edad_F + contador_edad_NB)
                porcentaje_NB = contador_edad_NB * 100 / (contador_edad_M + contador_edad_F + contador_edad_NB)
                
        promedio_edad_M = suma_edad_M / contador_edad_M
        promedio_edad_F = suma_edad_F / contador_edad_F
        promedio_edad_NB = suma_edad_NB / contador_edad_NB
        
        mensaje_1 = "Cantidad de postulantes de genero no binario (NB) que\nprograman en ASP.NET o JS cuya edad este entre 25 y 40,\nque se hayan postulado para un puesto Ssr: {0}\n".format(cantidad_postulantes_A)
        mensaje_2 = "Nombre del postulante Jr con menor edad: {0}\n".format(nombre_postulante_jr_menor_edad)
        mensaje_3 = "Promedio de edades por género\nM: {0}\nF: {1}\nNB: {2}\n".format(promedio_edad_M,promedio_edad_F,promedio_edad_NB)
        mensaje_4 = "Tecnología con más postulantes: {0}\n".format(tecnologia_con_mas_postulantes)
        mensaje_5 = "Porcentaje de postulantes de cada genero:\nM: {0}%\nF: {1}%\nNB: {2}%\n".format(porcentaje_M,porcentaje_F,porcentaje_NB)

        print(mensaje_1 + mensaje_2 + mensaje_3 + mensaje_4 + mensaje_5)    

        '''    
        
        
        respuesta_prompt= "si"

        while(respuesta_prompt != None):

            nombre_ingresado= prompt(title= "TP 07", prompt= "Ingrese su nombre")
            while (nombre_ingresado == None):
                nombre_ingresado= prompt(title= "TP 07", prompt= "Error, ingrese su nombre")

            edad_ingresada= prompt(title= "TP 07", prompt= "Ingrese su edad")
            while (edad_ingresada == None or int(edad_ingresada) < 18):
              edad_ingresada= prompt(title= "TP 07", prompt= "Error, ingrese su edad")
            edad_ingresada= int(edad_ingresada)

            genero_ingresado= prompt(title= "TP 07", prompt= "Ingrese su genero: F, M, NB")
            while ((genero_ingresado != "F" and genero_ingresado != "M" and genero_ingresado != "NB")or genero_ingresado == None):
                genero_ingresado= prompt(title= "TP 07", prompt= "Error, ingrese su genero: F, M, NB")

            tecnologia_ingresada= prompt(title= "TP 07", prompt="Ingrese un tipo de tecnologia: PYTHON - JS - ASP.NET")
            while ((tecnologia_ingresada != "PYTHON" and tecnologia_ingresada != "JS" and tecnologia_ingresada != "ASP.NET") or tecnologia_ingresada == None):
                tecnologia_ingresada= prompt(title= "TP 07", prompt="Error, ingrese un tipo de tecnologia")

            puesto_ingresado= prompt(title= "TP 07", prompt="Ingrese un puesto: Jr - Ssr - Sr")
            while ((puesto_ingresado != "Jr" and puesto_ingresado != "Ssr" and puesto_ingresado != "Sr") or puesto_ingresado == None):
                puesto_ingresado= prompt(title= "TP 07", prompt="Error, ingrese un puesto")

            


            for i in range(10):

                contador_postulantes_nb_ssr= 0
                bandera_primero= True
                contador_edad_f= 0
                sumatoria_edad_f= 0
                contador_edad_m= 0
                sumatoria_edad_m= 0
                contador_edad_nb= 0 
                sumatoria_edad_nb= 0
                sumatoria_postulantes_f= 0
                contador_postulantes_f= 0
                sumatoria_postulantes_m= 0
                contador_postulantes_m= 0
                sumatoria_postulantes_nb= 0
                contador_postulantes_nb= 0
                
                #A. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
                # cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
                
                match (puesto_ingresado):
                    case "Ssr":
                        match (genero_ingresado):
                            case "NB":
                                match (tecnologia_ingresada):
                                    case "ASP.NET" | "JS":
                                        if (edad_ingresada > 24 and edad_ingresada < 41):
                                            contador_postulantes_nb_ssr= contador_postulantes_nb_ssr + 1
        
            
                #B. Nombre del postulante Jr con menor edad.
                    case "Jr":
                        if (bandera_primero == True):
                            edad_menor = edad_ingresada
                            nombre_menor = nombre_ingresado
                            bandera_primero = False

                            if (edad_ingresada < edad_menor):
                                edad_menor = edad_ingresada
                                nombre_menor = nombre_ingresado

                #C. Promedio de edades por género.
                #E. Porcentaje de postulantes de cada genero.
                if (genero_ingresado == "F"):
                    contador_edad_f = contador_edad_f + 1
                    sumatoria_edad_f = sumatoria_edad_f + edad_ingresada
                    
                    sumatoria_postulantes_f = sumatoria_postulantes_f + i
                    contador_postulantes_f = contador_postulantes_f + 1   
                
                elif (genero_ingresado == "M"):
                    contador_edad_m = contador_edad_m + 1
                    sumatoria_edad_m = sumatoria_edad_m + edad_ingresada

                    sumatoria_postulantes_m = sumatoria_postulantes_m + i
                    contador_postulantes_m = contador_postulantes_m + 1      
                
                elif (genero_ingresado == "NB"):
                    contador_edad_nb = contador_edad_nb + 1
                    sumatoria_edad_nb = sumatoria_edad_nb + edad_ingresada

                    sumatoria_postulantes_nb = sumatoria_postulantes_nb + i
                    contador_postulantes_nb = contador_postulantes_nb + 1
                    

                #D. Tecnologia con mas postulantes (solo hay una)
                if (bandera_primero == True):
                    tecnologia_mas_postulantes = tecnologia_ingresada
                    bandera_primero = False

                    if (tecnologia_ingresada > tecnologia_mas_postulantes):
                        tecnologia_mas_postulantes = tecnologia_ingresada

            respuesta_prompt= prompt("TP 07", "¿Desea continuar?")

        promedio_edad_f = sumatoria_edad_f / contador_edad_f
        promedio_edad_m = sumatoria_edad_m / contador_edad_m
        promedio_edad_nb = sumatoria_edad_nb / contador_edad_nb

        porcentaje_postulantes_f = contador_postulantes_f * sumatoria_postulantes_f / 100
        porcentaje_postulantes_m = contador_postulantes_m * sumatoria_postulantes_m / 100
        porcentaje_postulantes_nb= contador_postulantes_nb * sumatoria_postulantes_nb / 100
                

        informe= f"Cantidad de postulantes genero NB, que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {contador_postulantes_nb_ssr}\n\
        Nombre del postulante Jr con menor edad: {nombre_menor}\n\
        Promedio de edad F: {promedio_edad_f}\n\
        Promedio de edad M: {promedio_edad_m}\n\
        Promedio de edad NB: {promedio_edad_nb}\n\
        Tecnologia con mas postulantes: {tecnologia_mas_postulantes}\n\
        Porcentaje de postulantes F: {porcentaje_postulantes_f}\n\
        Porcentaje de postulantes M: {porcentaje_postulantes_m}\n\
        Porcentaje de postulantes NB: {porcentaje_postulantes_nb}"

        print(informe)
        '''
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
