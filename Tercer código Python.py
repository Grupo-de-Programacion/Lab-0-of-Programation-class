# Definición de la función calcBmi
def calcBmi(altura, peso):
    # Calcular el índice de masa corporal (BMI)
    bmi = peso / ((altura / 100.0) ** 2)
    return bmi

# Función para calcular el peso ideal basado en la altura y un BMI normal (18.5 - 24.9)
def pesoIdeal(altura):
    # Convertir altura de centimetros a metros
    alturam = altura / 100.0
    # Calcular el peso ideal mínimo y máximo para un BMI de 18.5 a 24.9
    pesomin = 18.5 * (alturam ** 2)
    pesomax = 24.9 * (alturam ** 2)
    return pesomin, pesomax

# Punto de entrada principal

def vper():
    # Solicitar al usuario la altura en cms
    altura = float(input("Introduce tu altura en cms: "))

    # Solicitar al usuario el peso en kgs
    peso = float(input("Introduce tu peso en kgs: "))

    # Llamar a la función calcBmi
    bmi = calcBmi(altura, peso)

    # Mostrar el resultado
    print(f"Tu índice de masa corporal es {bmi} kg/m^2")
    if bmi < 18.5:
        print("Estás bajo de peso.")
        pesomin, pesomax = pesoIdeal(altura)
        print(f"Tu peso estaria en normalidad si estuviese entre {pesomin:} kg y {pesomax:} kg.")
    elif bmi >= 18.5 and bmi < 25:
        print("Tienes un peso normal.")
    elif bmi >= 25 and bmi < 30:
        print("Tienes sobrepeso.")
        pesomin, pesomax = pesoIdeal(altura)
        print(f"Tu peso estaria en normalidad si estuviese entre {pesomin:} kg y {pesomax:} kg.")
    else:
        print("Tienes obesidad.")
        pesomin, pesomax = pesoIdeal(altura)
        print(f"Tu peso estaria en normalidad si estuviese entre {pesomin:} kg y {pesomax:} kg.")

vper()
