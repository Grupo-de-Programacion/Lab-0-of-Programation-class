#include <stdio.h>

//  funciones
float calcBmi(float h, float w);
void calcPesoIdeal(float h, float *pesoMin, float *pesoMax);

int main(){
    // Declaración de variables locales
    float altura;
    float peso;
    float bmi;
    float pesoMin;
    float pesoMax;
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

        // Clasificación del BMI y cálculo del peso ideal
        if (bmi < 18.5){
            printf("Bajo peso\n");
            calcPesoIdeal(altura, &pesoMin, &pesoMax);
            printf("Para un peso normal, tu peso ideal deberia estar entre %f kg y %f kg\n", pesoMin, pesoMax);
        }
        if (bmi >= 25 && bmi < 30){
            printf("Sobrepeso\n");
            calcPesoIdeal(altura, &pesoMin, &pesoMax);
            printf("Para un peso normal, tu peso ideal deberia estar entre %f kg y %f kg\n", pesoMin, pesoMax);
        }
         if (bmi >= 30){
            printf("Obesidad\n");
            calcPesoIdeal(altura, &pesoMin, &pesoMax);
            printf("Para un peso normal, tu peso ideal deberia estar entre %f kg y %f kg\n", pesoMin, pesoMax);
        }
        else {
            printf("Peso normal\n");
        }
    }

    return 0;
}


// Implementación de la función calcBmi
float calcBmi(float h, float w){
    // Calcular el índice de masa corporal
    return w / ((h / 100.0) * (h / 100.0));

}

//función calcPesoIdeal
void calcPesoIdeal(float h, float *pesoMin, float *pesoMax){
    // Convertir altura de cm a metros
    float alturaMetros = h / 100.0;
    // Calcular el peso ideal para un BMI entre 18.5 y 24.9
    *pesoMin = 18.5 * (alturaMetros * alturaMetros);
    *pesoMax = 24.9 * (alturaMetros * alturaMetros);
}
