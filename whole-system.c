#include <stdio.h>
#include <stdlib.h>

struct Persona{
    char* Nombre;
    int Edad;
} p;

int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++) {
        if (i == 1) {
            int numero = atoi(argv[i]);
            printf("Tu numero + 5 es igual a: %d", numero + 5);  
        }
    }
    return 0;
}

