def Comparar_longitud (palabra1,palabra2):

    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
    resultado = longitud1 == longitud2
    return resultado

palabra1 = "Guadalupe"
palabra2 = "Armando"
longitudes = Comparar_longitud(palabra1,palabra2)

print (f'¿Son "{palabra1}" y "{palabra2}" dos palabras con la misma longitud? {longitudes}')

