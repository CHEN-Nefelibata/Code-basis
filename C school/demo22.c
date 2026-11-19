//数组
#include <stdio.h>
int main()
{
    int i,a[6];
    float avg;
    int sum=0;
    for(i=0;i<6;i++)
    {
        scanf("%d",&a[i]);
        sum+=a[i];
    }
    avg=sum/6.0;
    printf("%.2f",avg);
    return 0;
}