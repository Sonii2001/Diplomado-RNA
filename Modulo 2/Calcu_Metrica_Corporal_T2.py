def cabecera():
    titulo = """
======================================================
💪 CALCULADORA DE FITNESS Y SALUD PERSONAL 💪 

       🩺¡Descubre tus métricas de salud!🩺
======================================================
"""
    print(titulo)


def calcular_imc(peso, altura):
    """
    Calcula el IMC (Índice de Masa Corporal).
    Fórmula: IMC = peso / (altura^2)

    Parámetros:
    Peso_kg (float): Peso en kilogramos
    Altura_m (float): Altura en metros
    
    Retorna:
    Float: El IMC calculado
    """
    return peso / (altura ** 2)


def es_peso_saludable(imc):
    """
    Determina si el IMC está en rango saludable (18.5 - 24.9).

    Parámetro:
    Imc (float): Índice de Masa Corporal
    
    Retorna:
    Bool: True si está en rango saludable, False si no
    """
    return imc >= 18.5 and imc <= 24.9


def tiene_sobrepeso(imc):
    """
    Determina si hay sobrepeso (IMC >= 25).

    Parametro:
    Imc (float): El Índice de Masa Corporal calculado

    Retorna:
    True si hay sobrepeso (IMC ≥ 25)
    False si no hay sobrepeso (IMC < 25)
    """
    return imc >= 25


def tiene_bajo_peso(imc):
    """
    Determina si hay bajo peso (IMC < 18.5).

    Parametro:
    Imc (float): El Índice de Masa Corporal calculado

    Retorna:
    True si hay bajo peso (IMC ≥ 18.5)
    False si no hay bajo peso (IMC < 18.5)    
    """
    return imc < 18.5


def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict.
    FORMULA:
    Hombres: 88.362 + (13.397 × peso) + (4.799 × altura) - (5.677 × edad)
    Mujeres: 447.593 + (9.247 × peso) + (3.098 × altura) - (4.330 × edad)

    Parámetros:
    Peso_kg (float): Peso en kg
    Altura_cm (float): Altura en cm
    Edad (int): Edad en años
    Es_hombre (bool): True si es hombre, False si es mujer
    
    Retorna:
    float: Calorías diarias recomendadas
    """
    Calorias_Hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    Calorias_Mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)
    return es_hombre * Calorias_Hombre + (1 - es_hombre) * Calorias_Mujer
#print(f'Calorias diarias: {int(resultado)}')
#calorias = calcular_calorias_diarias(70, 175, 25, True)  

def calcular_agua_diaria(peso_kg):
    """
    Calcula litros de agua recomendados al día (35ml por kg de peso).

    Parametro:
    Peso_kg (float): Peso en kilogramos

    Retorna:
    Agua_diaria (float): Litros de agua recomendados
    """
    return (peso_kg * 35) / 1000
#agua_diaria = calcular_agua_diaria(80.0)

def calcular_ritmo_cardiaco_maximo(edad):
    """
    Calcula el ritmo cardíaco máximo (220 - edad).
    Formula:
    220 - edad

    Parametro:
    Edad (int): Edad en años

    Retorna:
    Ritmo_Cardiaco(int): Pulsaciones por minuto máximas recomendadas
    """
    return 220 - edad
#ritmo_cardiaco = calcular_ritmo_cardiaco_maximo(35)





# =================================
# APLICACIÓN PRINCIPAL
# =================================

cabecera()

# Pedir datos al usuario
nombre = input("📌 Cual es tu nombre? ")
peso = float(input("📌 Cuanto pesas (kg)? "))
altura = float(input("📌 Cuanto mides (Metros, ej: 1.80)? "))
edad = int(input("📌 Cuantos años tienes? "))
sexo = input("📌 Eres hombre o mujer (H/M)? ")

es_hombre = (sexo == "H")
altura_cm = altura * 100

# Calcular métricas
imc = calcular_imc(peso, altura)
calorias = calcular_calorias_diarias(peso, altura, edad, es_hombre)
agua = calcular_agua_diaria(peso)
ritmo_max = calcular_ritmo_cardiaco_maximo(edad)

# Mostrar resultados
print("\n================================================")
print("📊 REPORTE DE FITNESS Y SALUD 📊")
print("================================================")

# Datos Personales
print("\n✍  DATOS PERSONALES ✍")
print("------------------------")
print(f"Nombre: {nombre}")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"Edad: {edad} años")
print(f"Hombre: {es_hombre}")

# IMC
print("\n🙌 ÍNDICE DE MASA CORPORAL 🙌")
print("------------------------")
print(f"Tu IMC es: {imc:.2f}")

print("¿Peso saludable?", es_peso_saludable(imc))
print("¿Tienes sobrepeso?", tiene_sobrepeso(imc))
print("¿Tienes bajo peso?", tiene_bajo_peso(imc))

# Nutrición
print("\n🥗  NUTRICIÓN 🥗")
print("------------------------")
print(f"Calorías diarias recomendadas: {int(calorias)} kcal")
print(f"Agua recomendada al día: {agua:.2f} litros")

# Zona Cardíaca
print("\n💓 ZONA CARDÍACA 💓")
print("------------------------")
print(f"Ritmo cardíaco máximo: {ritmo_max} bpm")