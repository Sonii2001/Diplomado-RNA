def Calcular_Calorias(Carbohidratos, Proteinas, Grasas):
    """
    Se calcula el total de calorias(carbohidratos, proteinas y grasas)

    Parametros:
    Carbohidratos(int): 1 gramo equivale a 4 calorias
    Proteinas(int): 1 gramos equivale a 4 calorias
    Grasas(int): 1 gramo equivale a 9 calorias

    Retorna:
    Total(int): Cantidad total de calorias de una persona
    """

    resultado_total = (Carbohidratos * 4) + (Proteinas * 4) + (Grasas * 9)
    return resultado_total

calorias1 = Calcular_Calorias(10,40,5)
calorias2 = Calcular_Calorias(28,55,10)
calorias3 = Calcular_Calorias(5,25,2)

print(f"Calorias Totales: {calorias1}")
print(f"Calorias Totales: {calorias2}")
print(f"Calorias Totales: {calorias3}")