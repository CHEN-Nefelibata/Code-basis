//P1980：计数问题
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n,x;
    cin>>n>>x;
    int count=0;
    for(int i=1;i<=n;i++)
    {
        int d=i;
        while(d>0)
        {
            if(d%10==x)
                count++;
            d=d/10;
        }
    }
    cout<<count;
    return 0;
}