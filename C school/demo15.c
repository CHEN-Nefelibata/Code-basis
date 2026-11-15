#include <stdio.h>
int main()
{
    int i;
    long long j=1;
    double sum=0;
    for(i=1;i<=20;i++)
    {
        j*=i;
        sum+=j;
    }
    printf("%e",sum);
    return 0;
}