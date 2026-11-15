#include <stdio.h>
int main()
{
    double n;
    double sum=0.0;
    double h=100.0;
    scanf("%lf",&n);
    for(int i=1;i<=n;i++)
    {
        h=h/2.0;
        sum=sum+2*h;
        if(i<n)
        {
            sum+=h;
        }
    }
    printf("%.2lf %.2lf",sum,h);
    return 0;
}