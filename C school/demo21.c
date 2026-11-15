#include <stdio.h>
int main()
{
    int n,i,j,star;
    scanf("%d",&n);
    int mid=(n+1)/2;
    for(i=1;i<=n;i++)
    {
        if(i<=mid)
        {
            star=2*i-1;
        }
        else
        {
            star=2*(n-i+1)-1;
        }
        for(j=0;j<(n-star)/2;j++)
        {
            printf(" ");
        }
        for(j=0;j<star;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}