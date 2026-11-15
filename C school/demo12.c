#include <stdio.h>
int main()
{
    float x,y;
    scanf("%f %f",&x,&y);
    int h;
    if((x-2)*(x-2)+(y-2)*(y-2)<=1||(x+2)*(x+2)+(y-2)*(y-2)<=1||(x-2)*(x-2)+(y+2)*(y+2)<=1||(x+2)*(x+2)+(y+2)*(y+2)<=1)
        h=10;
    else 
        h=0;
    printf("%d",h);
    return 0;
}