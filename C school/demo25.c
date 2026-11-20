#include <stdio.h>
int main(){
    int a[5];
    int temp;
    for(int i=0;i<5;i++){
        scanf("%d",&a[i]);
    }
    for(int j=0;j<5/2;j++){
        temp=a[j];
        a[j]=a[4-j];
        a[4-j]=temp;
    }
    for(int i=0;i<5;i++){
        printf("%d ",a[i]);
    }
    return 0;
}