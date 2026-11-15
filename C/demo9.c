//建立求和函数
#include<stdio.h>
int Add(int x,int y)//定义求和函数
{   int z=0;
    z=x+y;
    return z;
    //或直接写 return x+y;   
}
int main(){
    int n1,n2=0;
    scanf("%d %d",&n1,&n2);
    int sum=Add(n1,n2);//调用函数
    printf("%d",sum);
    return 0;
}