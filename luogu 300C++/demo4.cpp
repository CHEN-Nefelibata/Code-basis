//P5716:月份天数
#include <bits/stdc++.h>
using namespace std;
int main(){
    int y,m;
    cin>>y>>m;
    int feb=28;
    if((y%4==0&&y%100!=0)||y%400==0) 
        feb=29;
    if(m==2)
        cout<<feb;
    else if(m==1||m==3||m==5||m==7||m==8||m==10||m==12)
        cout<<31;
    else
        cout<<30;
    return 0;
}