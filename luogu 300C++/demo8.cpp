//B2068：统计满足条件的4位数
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int cnt=0;
    while(n--)
    {
        int x;
        cin>>x;
        int q=x/1000;
        int b=x/100%10;
        int s=x/10%10;
        int g=x%10;
        if(g-q-b-s>0)
        {
            cnt++;
        }
    }
    cout<<cnt;
    return 0;
}