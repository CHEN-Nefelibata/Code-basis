#include <stdio.h>
#include <math.h>
int main(){
    float a;
    int c;
    scanf("%f",&a);
    if(a>0&&a<1000)
    {
        c=sqrt(a);
        printf("%d",c);
    }
    else
        printf("输入的数应为小于1000的正数。");
    return 0;
}