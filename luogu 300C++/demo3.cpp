//B3894:开车旅行
#include <bits/stdc++.h>
using namespace std;
int main(){
    double a,b,c,d;
    cin>>a>>b>>c>>d;
    double sum=a*b+c*d;
    double avg=sum/(b+d);
    printf("%.1lf\n",sum);
    printf("%.1lf\n",avg);
    return 0;
}