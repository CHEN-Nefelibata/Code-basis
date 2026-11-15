//6、定义最大值函数MAX
#include <stdio.h>
int Max(int a,int b)
{
    if(a>b)
        return a;
    else 
        return b;
}
int main(){
    int c,d=0;
    scanf("%d%d",&c,&d);
    int e=Max(c,d);
    printf("%d\n",e);
    return 0;
}