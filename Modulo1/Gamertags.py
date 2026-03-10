def cabecera():
    """Muestra la cabecera de la aplicacion"""
    titulo = """ .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    ______    | || |      __      | || | ____    ____ | || |  _________   | || |  _______     | || |  _________   | || |      __      | || |    ______    | || |    _______   | |
| |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | || | |_   __ \    | || | |  _   _  |  | || |     /  \     | || |  .' ___  |   | || |   /  ___  |  | |
| | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | || |   | |__) |   | || | |_/ | | \_|  | || |    / /\ \    | || | / .'   \_|   | || |  |  (__ \_|  | |
| | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | || |   |  __ /    | || |     | |      | || |   / ____ \   | || | | |    ____  | || |   '.___`-.   | |
| | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | || |  _| |  \ \_  | || |    _| |_     | || | _/ /    \ \_ | || | \ `.___]  _| | || |  |`\____) |  | |
| |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | || | |____| |___| | || |   |_____|    | || ||____|  |____|| || |  `._____.'   | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                                                                    👾 ¡Crea tu identidad gamer! 👾
 
 """
    print(titulo)
#cabecera()


def Crear_Tag_Basico(nombre):
    """
    CREA UN GAMETAG BASICO USANDO LAS PRIMERAS CUATRO LETRAS DEL NOMBRE.
    
    Parametro:
    nombre(str) : Nombre del usuario

    Retorna
    str : Gamertag Basico
    """
    tag = nombre[0:4] #slice
    return tag

#tag_basico = Crear_Tag_Basico("Sonia")
#print(tag_basico)


def Crear_Tag_Invertido(nombre):
    """
    CREA UN GAMETAG INVERTIDO USANDO EL NOMBRE COMPLETO.
    
    Parametro:
    nombre(str) : Nombre del usuario

    Retorna
    str : Gamertag Invertido
    """

    tag2 = nombre[::-1] #lo de adelante slice y lo ultimo stride
    return tag2
#tag_invertido = Crear_Tag_Invertido("Sonia")
#print(tag_invertido)

def Crear_Tag_Intercalado(nombre,apellido):
    """
    CREA UN GAMETAG INTERCALADO USANDO EL NOMBRE Y APELLIDO.
    
    Parametro:
    nombre(str) : Nombre del usuario
    apellido(str) : Apellido del usuario

    Retorna
    None (imprime directamente)
    """

    inicial_nombre = nombre [0]  #indexacion
    inicial_apellido = apellido[0]
    resto_nombre = nombre [1:]
    resto_apellido = apellido [1:]
    print("3. TAG INTERCALADO: ", inicial_nombre, inicial_apellido, resto_nombre, resto_apellido, sep="")

    #return nicial_nombre + inicial_apellido + resto_nombre + resto_apellido
#tag_intercalado = Crear_Tag_Intercalado("Sonia","Alvarado")
#print(tag_intercalado, sep = "")

def Crear_Tag_ELite (nombre):
    """
    CREA UN GAMETAG ELITE USANDO EL NOMBRE.
    
    Parametro:
    nombre(str) : Nombre del usuario

    Retorna
    None (imprime directamente)
    """
    primeras_nombre = nombre[:2]
    ultimas_nombre = nombre[-2:]
    print("4. TAG ELITE: ", primeras_nombre, ultimas_nombre, sep="")

    #return primeras_nombre + ultimas_nombre

#tag_elite = Crear_Tag_ELite("Sonia")
#print(tag_elite)

def Crear_Tag_Con_Numero(nombre,numero_fav):
   """
   CREA UN GAMETAG CON NUMERO USANDO EL NOMBRE Y NUMERO FAVORITO.
    
   Parametro:
   nombre(str) : Nombre del usuario
   numero(int) : Numero favorito del usuario

   Retorna
   None (imprime directamente)
   """
   numero_fav = 7
   print("5. TAG CON NUMERO: ", nombre[:5], numero_fav)

tag_numero = Crear_Tag_Con_Numero()

def Mostrar_Estadisticas (nombre):
    """
    MUESTRA ESTADISTICAS DEL NOMBRE PROPORCIONADO
    
    Parametro:
    nombre(str) : Nombre del usuario a analizar

    Retorna
    None (imprime directamente)
    """   
    long_nombre = len(nombre)

    print("\nESTADISTICAS DE TU NOMBRE")
    print("Nombre completo:", nombre)
    print("La longitud del nombre:", long_nombre)
    print("Primera letra:", nombre[0])
    print("Ultima letra:", nombre[-1])

def Generar_todas_funciones(nombre,apellido,numero):
    """
    MGENERA Y MUESTRA TODAS LAS OPCIONES DE GAMERTAGS
    
    Parametro:
    nombre(str) : Nombre del usuario 
    apellido(str) : Apellido del usuario
    numero(str) : Numero favorito del usuario

    Retorna
    None (imprime directamente)
    """  

    print("\n==============================================================================")
    print(" TUS OPCIONES DE GAMERTAG: ")
    print("\n==============================================================================")

    tag = Crear_Tag_Basico(nombre)
    print("\n1. TAG BASICO:", tag)
    print("\n2. TAG INVERTIDO:", Crear_Tag_Invertido(nombre))
    Crear_Tag_Intercalado(nombre,apellido)
    Crear_Tag_ELite(nombre)


    print("\n =============================================================================")

# =================================================================================
# APLICACION PRINCIPAL
# =================================================================================
# llamar a la funcion cabecera
cabecera()

## SOLICITAR DATOS AL USUARIO
nombre = input("\n Introduce tu nombre: ")
apellido = input("\n Introduce tu apellido: ")
numero = input("\n Introduce tu numero favorito: ")

## MOSTRAR ESTADISTICAS DEL USUARIO
Mostrar_Estadisticas(nombre)
Generar_todas_funciones(nombre,apellido,numero)

## MENSAJE FINAL
print("\n   ¡ELIGE TU FAVORITO Y CONQUISTA EL MUNDO GAMER!         \n")



