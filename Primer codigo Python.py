# Definición de la función calcBmi
def calcBmi(altura, peso):
    # Calcular el índice de masa corporal (IMC)
    bmi = peso / ((altura / 100.0) ** 2)
    return bmi

def vper():
    # Solicitar al usuario la altura en cms
    altura = float(input("Introduce tu altura en cms: "))

    # Solicitar al usuario el peso en kgs
    peso = float(input("Introduce tu peso en kgs: "))

    # Llamar a la función calcBmi
    bmi = calcBmi(altura, peso)

    # Mostrar el resultado
    print(f"Tu índice de masa corporal es {bmi} kg/m^2")
    if bmi<18.5:
        print("bajo de peso")
    if bmi>=18.5 and bmi <25:
        print("peso normal.")
    if bmi>=25 and bmi <30:
        print("sobrepeso.")
    if bmi>=30:
        print("obesidad.")
