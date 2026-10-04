#include <stdio.h>
#include <math.h>

int main() {
    double x0 =0.5;
    double x1 =(1.0 + x0)/(1.0 + exp(x0));
    printf("First approximation (x0) = %.2f\n",x0);
    printf("Second approximation (x1) = %.2f\n",x1);
    
    return 0;
}
