// #include <stdio.h>
// #include <math.h>
// int main()
// {
//     int a,n;
//     scanf("%d\n%d",&a,&n);
//     double s=a/9.0*10*(pow(10,n)-1)/9.0-a/9.0*n;
//     printf("%.0f",s);
//     return 0;
// }
#include <stdio.h>
#include <math.h>
int main()
{
    int a,n;
    long long sum=0;
    long long temp=0;
    scanf("%d\n%d",&a,&n);
    for(int i=1;i<=n;i++)
    {
        temp=temp*10+a;
        sum+=temp;
    }
    printf("%lld",sum);
    return 0;
}