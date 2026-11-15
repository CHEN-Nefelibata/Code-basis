//P1085:不高兴的津津
#include <bits/stdc++.h>
using namespace std;
int main(){
    int max_time=0;
    int ans=0;
    for(int i=1;i<=7;i++)
    {
        int a,b;
        cin>>a>>b;
        if(a+b>8&&a+b>max_time)
        {
            ans=i;
            max_time=a+b;
        }
    }
    cout<<ans;
    return 0;
}