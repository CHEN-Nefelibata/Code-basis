#include <stdio.h>
int main()
{
    float a[10];
    float max,min;
    int maxi,mini;
    for(int i=0;i<10;i++)
        scanf("%f",&a[i]);
    for(int i=0;i<10;i++)
    {
        if(i==0)
        {
            max=a[i];
            min=a[i];
            maxi=i;
            mini=i;
        }
        else
        {
            if(a[i]>max)
            {
                max=a[i];
                maxi=i;
            }
            if(a[i]<min)
            {
                min=a[i];
                mini=i;
            }
        }
    }
    printf("%.1f %d %.1f %d",max,maxi,min,mini);
    return 0;
}