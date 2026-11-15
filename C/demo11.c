//C语言中0为假，非0为真
#include <stdio.h>
int main(){
    int a = 10;
    int b = a++;//先b=a，再a=a+1；即为先赋值后递加，为后++
    printf("%d\n",b);//10
    printf("%d\n",a);//a+1=11
    int c = 10;
    int d=++c;//先c=c+1，d=c；即为先递加再赋值，为先++
    printf("%d\n",c);//c+1=11
    printf("%d\n",d);//11
    float pi=3.14;
    int e=(int)pi;//(类型)表示强制类型转化
    printf("%d\n",e);
    int f=10;
    int g=20;
    if(f&&g)//&&为并且，判断两边是否都为真则输出，若有一边为假则不输出
    {
        printf("hehe\n");
    }
    int h=0;
    int i=10;
    if(h||i)//||表示或者，判断只要有一边为真则输出
    {
        printf("hehe\n");
    }
    return 0;
}