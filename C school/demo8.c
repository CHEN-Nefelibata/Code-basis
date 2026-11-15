#include <stdio.h>
int main()
{
    int a=3,b=4,c=5;
    int x,y;
    int x1=a+b>c && b==c;
    int x2=a||b+c && b-c;
    int x3=!(a>b) && !c||1;
    int x4=!(x=a) && (y=b) && 0;
    int x5=!(a+b)+c-1 && b+c/2;
    printf("%d %d %d %d %d",x1,x2,x3,x4,x5);
    return 0;
}