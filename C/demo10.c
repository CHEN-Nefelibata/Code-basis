//数组
#include <stdio.h>
int main(){
    int arr[10]={10,11,12,13,14,15,16,17,18,19};//为int类型的数组//可将变量置于[]中，但不能初始化
    char ch[12]={"hello world"};//为char定义的字符，用字符串表示，加上空格和'\0'共12个字符
    //printf("%d\n",arr[8]);输出数组中第八个元素
    int i=0;
    while(i<10){
        printf("%d ",arr[i]);//循环输出0-9下标代表的数
        i+=1;//i++;
    }
    return 0;
}