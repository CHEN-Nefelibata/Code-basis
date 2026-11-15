//while循环
#include <stdio.h>
int main(){
    int line=0;
    while(line <20000){
        printf("写代码\n");
        line++;//不断积累的过程，累加
    }
    if (line>=20000)
    {
        printf("好offer\n");
    }
    else
    {
        printf("继续加油\n");
    }
    return 0;
}