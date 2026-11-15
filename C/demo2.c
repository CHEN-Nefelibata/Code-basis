/*char 字符类型，%c打印字符，%s打印字符串
short 短整型
int 整型,%d打印整形
long 长整型
long long 长长整型
float 单精度浮点型，%f打印浮点型
double 双精度浮点型，%lf打印双精度浮点型
long double 长双精度浮点型
%zu打印sizeof()的结果
变量局部优先
*/
#include <stdio.h>
int main(){
    int a =10;
    printf("%d\n",a);
    printf("%d\n",sizeof(a));
    printf("%d\n",sizeof(int));
    printf("%d\n",sizeof a);//计算类型大小同前两行
    return 0;
}