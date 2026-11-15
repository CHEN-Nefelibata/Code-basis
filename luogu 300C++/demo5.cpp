//P5718:找最小值
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int ans=1000;
    while(n--){
        int a;
        cin>>a;
        if(ans>a)
        {
            ans=a;
        }
    }
    cout<<ans<<endl;
    return 0;
}