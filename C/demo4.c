//#define _CRT_SECURE_NO_WARNINGS 1 定义正常环境
//extern 用于声明外部变量的函数
//字面常量即常量
//const修饰的常量为固定一个变量不会被改变，即常变量不等于常量，本质仍为变量
//define标识符常量相当于全局变量,但不定义其类型,等同于常变量
//enum定义的枚举常量，仅作为列举，不能参与赋值
#define MAX 100
#define STR "hello world"
#include <stdio.h>
int main(){
    const int a=10;
    //a=20;会报错，const赋予下a的值无法改变。
    printf("%d\n",a);
    printf("%d\n",MAX);
    int b=MAX;
    printf("%d\n",b);
    char c[]=STR;
    printf("%s\n",STR);
    printf("%s\n",c);
    enum color { RED, GREEN, BLUE };
    enum color d=RED;
    return 0;
}