//4、逆序三位数
#include <stdio.h>
int main(){
    int a=0;
    scanf("%d",&a);
    int baiwei=a/100;
    int shiwei=(a/10)%10;
    int gewei=a%10;
    int sum=gewei*100+shiwei*10+baiwei;
    printf("%d\n",sum);
    return 0;
}