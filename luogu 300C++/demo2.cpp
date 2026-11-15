//B3685:计算
#include <bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c,d,s;
    cin>>a;
    b=a/100;//百位
    c=a/10%10;//十位
    d=a%10;//个位
    s=b+c+d;
    cout<<s<<endl;
    cout<<s*s<<endl;
    cout<<s*s*s<<endl;
    return 0;
}