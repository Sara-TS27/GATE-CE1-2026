#include <stdio.h>
#include <math.h>

int main(void) 
{
    double x0 = 0.5;
    double x1 = (1.0 + x0) / (1.0 + exp(x0));

    // %f formatted to 6 decimal places for numerical accuracy
    printf("First approximation  (x0) = %.4f\n", x0);
    printf("Second approximation (x1) = %.4f\n", x1);
    
    return 0;
}
