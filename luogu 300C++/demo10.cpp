//B3841:自幂数判断
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int m;
    cin>>m;
    while(m--)
    {
        int a;
        cin>>a;
        int p=0;
        int n=a;
        while(n){
            n/=10;
            ++p;
        }
        int sum=0;
        n=a;
        while(n){
            int b=n%10;
            sum+=pow(b,p);
            n/=10;
        }
        if(sum==a)
            cout<<"T"<<endl;
        else
            cout<<"F"<<endl;
    }
    return 0;
}