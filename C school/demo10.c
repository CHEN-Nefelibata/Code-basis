#include <stdio.h>
int main()
{
    int i;
    int price;
    scanf("%d",&i);
    if(i>=0&&i<=100000)
        price=i*0.1;
    else if(i>100000&&i<=200000)
        price=10000+(i-100000)*0.075;
    else if(i>200000&&i<=400000)
        price=17500+(i-200000)*0.05;
    else if(i>400000&&i<=600000)
        price=27500+(i-400000)*0.03;
    else if(i>600000&&i<=1000000)
        price=33500+(i-600000)*0.015;
    else 
        price=39500+(i-1000000)*0.01;
    printf("%d",price);
    return 0;
}