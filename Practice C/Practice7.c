//7、定义函数
#include <stdio.h>
int f(int x)
{
    if(x<0)
        return 1;
    else if(x==0)
        return 0;
    else
        return -1;
}
int main(){
    int a=0;
    scanf("%d",&a);
    int r=f(a);
    printf("%d",r);
    return 0;
}