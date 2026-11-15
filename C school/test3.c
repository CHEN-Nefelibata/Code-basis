#include <stdio.h>
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