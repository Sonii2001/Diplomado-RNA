def Contar_Caracteres(frase):
    long = len(frase)
    print(f'La frase "{frase}" tiene {long} caracteres')
    print()

Contar_Caracteres("Este ejercicio es del TEMA: FUNCIONES PROPIAS DE PYTHON")

def Convertir_Numero(entero):
    print(f'1. Entero: {entero}, Tipo: {type(2001)}')
    print(f'2. Cadena: {str(entero)}, Tipo: {type("2001")}')
    print(f'3. FLotante: {float(entero)}, Tipo: {type(2001.0)}')

Convertir_Numero(2001)
