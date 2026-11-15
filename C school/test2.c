//辗转相除法
#include <stdio.h>
int main()
{
    int m,n,r,temp,x,y;
    scanf("%d %d",&m,&n);
    temp=m*n;
    while(n!=0)
    {
        r=m%n;
        m=n;
        n=r;
    }
    x=m;
    y=temp/x;
    printf("%d %d",x,y);
    return 0;
}