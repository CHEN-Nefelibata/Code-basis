#include <stdio.h>
int main(){
    int a=10;
    int b=20;
    int r=a>b?a:b;//exp1？exp2：exp3中？表示先判断exp1是否成立，若成立则执行exp2，若不成立则执行exp3
    printf("%d\n",r);
    //逗号表达式
    int c=10;
    int d=20;
    int e=0;
    int f=(e=c-2,c=d+e,e-3);//从左向右依次计算，整体表达式结果为最后一个表达式的结果
    printf("%d\n",f);
    return 0;
}