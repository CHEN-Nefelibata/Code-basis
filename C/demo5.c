//char 表示字符类型，''表示字符常量，" "表示字符串常量
#include <stdio.h>
#include <string.h>
int main(){
    char a='A';
    char b[]="abcdef";//[]表示字符数组，末尾有一个'\0'表示结束
    char c[]={'a','b','c','d','e','f','\0'};//字符数组，末尾没有'\0'表示结束
    printf("%c\n",a);
    printf("%s\n",b);
    printf("%s\n",c);//重复输出，需单独加入\0来结束
    int d=strlen(c);//strlen()函数用于计算字符串的长度，返回值为int类型，需要添加#include <string.h>头文件
    printf("%d\n",d);
    return 0;
}