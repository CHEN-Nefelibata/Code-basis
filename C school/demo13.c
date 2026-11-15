#include <stdio.h>
int main()
{
    double sum1=0;
    double sum2=0;
    double sum3=0;
    double sum=0;
    for(int i=1;i<=100;i++)
        sum1+=i;
    for(int j=1;j<=50;j++)
        sum2+=j*j;
    for(int k=1;k<=10;k++)
        sum3+=1.0/k;
    sum=sum1+sum2+sum3;
    printf("%.2f",sum);
    return 0;
}