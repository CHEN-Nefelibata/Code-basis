//水仙花数
#include <stdio.h>
int main()
{
    int i,a,b,c;
    int count=0;
    for(i=100;i<=999;i++)
    {
        a=i/100;
        b=i/10%10;
        c=i%10;
        if(i==a*a*a+b*b*b+c*c*c)
        {    
            printf("%d\n",i);
            count++;
            if(count==3)
                break;
        }

    }
    return 0;
}