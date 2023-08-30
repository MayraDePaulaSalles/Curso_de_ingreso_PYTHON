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
A) El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con 
 algunos pokemones de prueba.

Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Tierra, Psiquico, Fuego, Electrico)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)
    
-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

*******Tener en cuenta que pueden no haber ingresos o egresos**********
C) Al presionar el boton Informar 
    # 0) - Cantidad de pokemones de tipo Fuego
    # 1) - Cantidad de pokemones de tipo Electrico
    # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
    # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
    # 4) - Cantidad de pokemones, con mas de 100 de poder.
    # 5) - Cantidad de pokemones, con menos de 100 de poder
    # 6) - tipo de los pokemones del tipo que mas pokemones posea 
    # 7) - tipo de los pokemones del tipo que menos pokemones posea 
    # 8) - el promedio de poder de todos los ingresados
    # 9) - el promedio de poder de todos los poquemones de Electrico 

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

        self.lista_nombre = ["Charmander","Pikachu","Squirtle","Wooper","Chimecho","Kadabra","Blastoise"]
        self.lista_tipo = ["Fuego","Electrico","Agua","Agua","Psiquico","Psiquico","Agua"]
        self.lista_poder = [120,130,100,80,70,110,90]


    def btn_cargar_on_click(self):
        # PUNTO A
        respuesta_prompt= "si"

        while(respuesta_prompt != None):
           
            nombre_pokemon= prompt(title= "Simulacro", prompt= "Ingrese su nombre")
            while (nombre_pokemon == None):
                nombre_pokemon= prompt(title= "Simulacro", prompt= "Error, ingrese su nombre")
            self.lista_nombre.append(nombre_pokemon)

            tipo_elemento= prompt(title= "Simulacro", prompt= "Ingrese su tipo de elemento: Agua, Tierra, Psiquico, Fuego, Electrico")
            while (not tipo_elemento.isalpha() or (tipo_elemento != "Agua" and tipo_elemento != "Tierra" and tipo_elemento != "Psiquico" and tipo_elemento != "Fuego" and tipo_elemento != "Electrico")or tipo_elemento == None):
                tipo_elemento= prompt(title= "Simulacro", prompt= "Error, ingrese su tipo de elemento: Agua, Tierra, Psiquico, Fuego, Electrico")
            self.lista_tipo.append(tipo_elemento)

            cantidad_poder= prompt(title= "Simulacro", prompt= "Ingrese la cantidad de poder")
            while (cantidad_poder == None or int(cantidad_poder) < 50 and int(cantidad_poder) > 200):
              cantidad_poder= prompt(title= "Simulacro", prompt= "Error, ingrese la cantidad de poder")
            cantidad_poder= int(cantidad_poder)
            self.lista_poder.append(cantidad_poder)



            respuesta_prompt= prompt("Simulacro", "¿Desea continuar?")
    
    def btn_mostrar_on_click(self):
        # PUNTO B
        bandera_primero= True
        lista_cantidad_poder= self.lista_poder
        lista_tipo_elemento= self.lista_tipo 
        lista_nombre_pokemon= self.lista_nombre
            
        #Al presionar el boton mostrar, se debera mostrar el pokemon (nombre, tipo y poder) de tipo fuego o agua con mas poder
        for i in range(len(self.lista_tipo)):
            if (self.lista_tipo[i] == "Fuego" or self.lista_tipo[i] == "Agua"):
                if(bandera_primero == True):
                    max_cantidad_poder_f_a = lista_cantidad_poder[0]
                    max_tipo_elemento_f_a = lista_tipo_elemento[0]
                    max_nombre_pokemon_f_a = lista_nombre_pokemon[0]
                    bandera_primero = False
                    
                    if(lista_cantidad_poder[i] > max_cantidad_poder_f_a):
                        max_cantidad_poder_f_a = lista_cantidad_poder[i]
                        max_tipo_elemento_f_a = lista_tipo_elemento[i]
                        max_nombre_pokemon_f_a= lista_nombre_pokemon[i]

        
        mensaje= f"El nombre del pokemon con mas poder de tipo fuego o agua es:{max_nombre_pokemon_f_a}\nSu elemento es:{max_tipo_elemento_f_a}\nSu cantidad de poder es: {max_cantidad_poder_f_a}"  
        print(mensaje)
        
    def btn_informar_on_click(self):
        #PUNTO C
        #0) - Cantidad de pokemones de tipo Fuego
        contador_fuego= 0
        contador_electrico= 0
        for i in range(len(self.lista_tipo)):
            if (self.lista_tipo[i] == "Fuego"):
                contador_fuego= contador_fuego + 1
        # 1) - Cantidad de pokemones de tipo Electrico
            elif (self.lista_tipo[i] == "Electrico"):
                contador_electrico= contador_electrico + 1

        mensaje_1= f"Cantidad de pokemones de tipo Fuego: {contador_fuego}\nCantidad de pokemones de tipo Electrico: {contador_electrico}"
        #print(mensaje_1)
            
            
        bandera_primero= True
        lista_cantidad_poder= self.lista_poder
        largo_lista_poder= len(self.lista_poder)
        lista_tipo_elemento= self.lista_tipo 
        lista_nombre_pokemon= self.lista_nombre
        
        # Realizar informe 2
        # 2) - Nombre, tipo y Poder del pokemon con el poder mas alto
        # 3) - Nombre, tipo y Poder del pokemon con el poder mas bajo
        if (bandera_primero == True):
            max_cantidad_poder = lista_cantidad_poder[0]
            max_tipo_elemento = lista_tipo_elemento[0]
            max_nombre_pokemon = lista_nombre_pokemon[0]
            min_cantidad_poder = lista_cantidad_poder[0]
            min_tipo_elemento = lista_tipo_elemento[0]
            min_nombre_pokemon = lista_nombre_pokemon[0]
            bandera_primero = False

            for i in range(largo_lista_poder):
                if (lista_cantidad_poder[i] > max_cantidad_poder):
                    max_cantidad_poder = lista_cantidad_poder[i]
                    max_tipo_elemento = lista_tipo_elemento[i]
                    max_nombre_pokemon = lista_nombre_pokemon[i]
                
                elif (lista_cantidad_poder[i] < min_cantidad_poder):
                    min_cantidad_poder = lista_cantidad_poder[i]
                    min_tipo_elemento = lista_tipo_elemento[i]
                    min_nombre_pokemon = lista_nombre_pokemon[i]
                

        mensaje_2= f"El nombre del pokemon con mas poder es:{max_nombre_pokemon}, su elemento es:{max_tipo_elemento} y su cantidad de poder es: {max_cantidad_poder}\nEl nombre del pokemon con menos poder es:{min_nombre_pokemon} su elemento es:{min_tipo_elemento}, su cantidad de poder es: {min_cantidad_poder}"
        #print(mensaje_2)

        # 4) - Cantidad de pokemones, con mas de 100 de poder.
        contador_pokemones_mas_cien_poder= 0
        contador_pokemones_menos_cien_poder= 0
        for i in range(len(self.lista_poder)):
            if (self.lista_poder[i] > 100):
                contador_pokemones_mas_cien_poder= contador_pokemones_mas_cien_poder + 1
        # 5) - Cantidad de pokemones, con menos de 100 de poder
            elif (self.lista_poder[i] < 100):
                contador_pokemones_menos_cien_poder= contador_pokemones_menos_cien_poder + 1   

        mensaje_3= f"Cantidad de pokemones, con mas de 100 de poder: {contador_pokemones_mas_cien_poder}\nCantidad de pokemones, con menos de 100 de poder: {contador_pokemones_menos_cien_poder}"
        #print(mensaje_3)

        # 6) - tipo de los pokemones del tipo que mas pokemones posea 
        # 9-2 = 7
        # 7) - tipo de los pokemones del tipo que menos pokemones posea
        contador_agua= 0
        contador_tierra= 0
        contador_psiquico= 0
        contador_fuego= 0
        contador_electrico= 0
        for i in range(len(self.lista_tipo)):
            
            match (self.lista_tipo[i]):
                case "Agua":
                    contador_agua= contador_agua + 1
                case "Tierra":
                    contador_tierra= contador_tierra + 1
                case "Psiquico":
                    contador_psiquico= contador_psiquico + 1
                case "Fuego": 
                    contador_fuego= contador_fuego + 1
                case "Electrico":
                    contador_electrico= contador_electrico + 1

        if (contador_agua > contador_tierra and contador_agua > contador_psiquico and contador_agua > contador_fuego and contador_agua > contador_electrico):
            mayor_cantidad_por_tipo= "Agua"
        elif (contador_tierra > contador_agua and contador_tierra > contador_psiquico and contador_tierra > contador_fuego and contador_tierra > contador_electrico):
            mayor_cantidad_por_tipo= "Tierra"
        elif (contador_psiquico > contador_agua and contador_psiquico > contador_tierra and contador_psiquico > contador_fuego and contador_psiquico > contador_electrico):
            mayor_cantidad_por_tipo= "Psiquico"
        elif (contador_fuego > contador_agua and contador_fuego > contador_tierra and contador_fuego > contador_psiquico and contador_fuego > contador_electrico):
            mayor_cantidad_por_tipo= "Fuego"
        elif (contador_electrico > contador_agua and contador_electrico > contador_tierra and contador_electrico > contador_psiquico and contador_electrico > contador_fuego):
            mayor_cantidad_por_tipo= "Electrico"

        if (contador_agua < contador_tierra and contador_agua < contador_psiquico and contador_agua < contador_fuego and contador_agua < contador_electrico):
            menor_cantidad_por_tipo= "Agua"
        elif (contador_tierra < contador_agua and contador_tierra < contador_psiquico and contador_tierra < contador_fuego and contador_tierra < contador_electrico):
            menor_cantidad_por_tipo= "Tierra"
        elif (contador_psiquico < contador_agua and contador_psiquico < contador_tierra and contador_psiquico < contador_fuego and contador_psiquico < contador_electrico):
            menor_cantidad_por_tipo= "Psiquico"
        elif (contador_fuego < contador_agua and contador_fuego < contador_tierra and contador_fuego < contador_psiquico and contador_fuego < contador_electrico):
            menor_cantidad_por_tipo= "Fuego"
        elif (contador_electrico < contador_agua and contador_electrico < contador_tierra and contador_electrico < contador_psiquico and contador_electrico < contador_fuego):
            menor_cantidad_por_tipo= "Electrico"
  
    
        mensaje_4= f"La mayor cantidad de pokemones por elemento es: {mayor_cantidad_por_tipo}\nLa menor cantidad de pokemones por elemento es:{menor_cantidad_por_tipo}"
        #print(mensaje_4)

        # 8) - el promedio de poder de todos los ingresados
        acumulador_poder= 0
        contador_pokemones= len(self.lista_nombre) 
        for i in range(len(self.lista_poder)):
            acumulador_poder= acumulador_poder + self.lista_poder[i]
        
        promedio_poder_pokemones= acumulador_poder / contador_pokemones

        mensaje_5= f"El promedio de poder de todos los ingresados: {promedio_poder_pokemones}"
        #print(mensaje_5)

        # 9) - el promedio de poder de todos los pokemones de Electrico
        acumulador_poder_electrico= 0
        contador_electrico= 0
        for i in range(len(self.lista_tipo)):
            if(self.lista_tipo[i] == "Electrico"):
                acumulador_poder_electrico= acumulador_poder_electrico + self.lista_poder[i]
                contador_electrico= contador_electrico + 1

        if (contador_electrico != 0):
            promedio_poder_electrico= acumulador_poder_electrico / contador_electrico
        else:
            promedio_poder_electrico= 0

        mensaje_6= f"El promedio de poder de los pokemones del tipo electrico es: {promedio_poder_electrico}"
        #print(mensaje_6)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
