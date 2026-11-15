//if语句
#include <stdio.h>
int main(){
    int input=0;
    printf("要好好学习吗？(0/1)");
    scanf("%d",&input);
    if(input == 1){
        printf("拿到大厂offer");
    }
    else {
        printf("卖红薯");
    }
    return 0;
}