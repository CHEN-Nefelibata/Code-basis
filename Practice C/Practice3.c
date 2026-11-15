//3、时间加减转换
#include <stdio.h>
int main(){
    int a,b=0;
    scanf("%d %d",&a,&b);
    int c=a/100*60+a%100;
    int d=(c+b)/60;
    int e=(c+b)%60;
    printf("%d\n",d*100+e);
    return 0;
}