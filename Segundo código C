#include <stdio.h>

// Prototipo de la función calcBmi
float calcBmi(float h, float w);

// Función principal - punto de entrada
int main(){
    // Declaración de variables locales
    float altura;
    float peso;
    float bmi;
    int n;
    int i;

    // Pedir el número de personas
    printf("Introduce el numero de personas: ");
    scanf("%d", &n);

    // Ciclo
    for(i = 0; i < n; i++) {
        printf("\nIntroduce la altura en cm para la persona %d: ", i + 1);
        scanf("%f", &altura);

        printf("Introduce el peso en kg para la persona %d: ", i + 1);
        scanf("%f", &peso);

        // Calcular el BMI
        bmi = calcBmi(altura, peso);

        // BMI de la persona actual
        printf("Persona %d - BMI: %.2f kg/m^2\n", i + 1, bmi);

        // Clasificación del BMI
        if (bmi < 18.5){
            printf("Bajo peso\n");
        }
        if (bmi >= 18.5 && bmi < 25){
            printf("Peso normal\n");
        }
        if (bmi >= 25 && bmi < 30){
            printf("Sobrepeso\n");
        }
        if (bmi >= 30){
            printf("Obesidad\n");
        }
    }

    return 0;
}

// Implementación de la función calcBmi
float calcBmi(float h, float w){
    // Calcular el índice de masa corporal
    return w / ((h / 100.0) * (h / 100.0));
}
