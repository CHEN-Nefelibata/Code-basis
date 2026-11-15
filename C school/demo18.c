#include <stdio.h>
int main()
{
    int n;
    double sum=0.0;
    double a=2,b=1;
    double temp;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        sum+=a/b;
        temp=a;
        a=a+b;
        b=temp;
    }   
    printf("%.4f",sum);
    return 0;
}