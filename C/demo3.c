#include <stdio.h>
int main(){
    int num1=0;
    int num2=0;
    scanf("%d %d",&num1,&num2);//输入两个整数，&表示输入地址
    int sum=num1+num2;//求和
    printf("%d\n",sum);
    return 0;
}