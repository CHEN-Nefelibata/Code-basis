//\表示下的转义字符
#include <stdio.h>
int main()
{
    printf("abc\n");//\n表示换行符，输出后换行
    printf("abc");
    printf("abc0def\n");
    printf("abc\0def");//\0表示字符串结束符，输出后不再输出后面的字符
    printf("abc\\def\n");//\\表示输出一个\,防止被误认为是转义字符
    printf("abc\tdef\n");//\t表示制表符，输出后制表即空格
    printf("abc\"def\n");//\"表示输出一个"，防止被误认为是字符串结束符
    printf("abc\'def\n");//\'表示输出一个'，防止被误认为是字符结束符
    printf("abc\rdef\n");//\r表示回车符，输出后光标回到行首
    printf("abc\fdef\n");//\f表示换页符，输出后换页
    printf("abc\bdef\n");//\b表示退格符，输出后光标回到前一个位置
    printf("abc\vdef\n");//\v表示垂直制表符，输出后光标下移一行
    printf("abc\?def\n");//\?表示输出一个?，防止被误认为是三字符序列
    printf("abc\adef\n");//\a表示响铃符，输出后发出提示音
    return 0;
}