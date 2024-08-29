#include <stdio.h>

// función calcBmi
float calcBmi(float h, float w);

// Función principal
int main(){
    // Declaración de variables
    float altura;
    float peso;
    float bmi;

    // Pedir al usuario la altura en cm
    printf("Introduce tu altura en cm: ");
    scanf("%f", &altura);

    // Pedir al usuario el peso en kg
    printf("Introduce tu peso en kg: ");
    scanf("%f", &peso);

    // función calcBmi
    bmi = calcBmi(altura, peso);

    // Imprimir el resultado
    printf("Tu indice de masa corporal es %.2f kg/m^2\n", bmi);

    // Clasificación del BMI
    if (bmi < 18.5){
        printf("Estas bajo de peso\n");
    }
    if (bmi >= 18.5 && bmi < 25){
        printf("Tienes un peso normal\n");
    }
    if (bmi >= 25 && bmi < 30){
        printf("Tienes sobrepeso\n");
    }
    if (bmi >= 30){
        printf("Tienes obesidad\n");
    }

    return 0;
}

// Implementación de la función calcBmi
float calcBmi(float h, float w){
    float bmi;

    // Calcular el índice de masa corporal
    bmi = w / ((h / 100.0) * (h / 100.0));
    return bmi;
}
