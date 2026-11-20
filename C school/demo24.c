//初步冒泡排序
#include <stdio.h>
int main(){
    float a[8];
    for(int i=0;i<8;i++){
        scanf("%f",&a[i]);
    }
    for(int i=0;i<8;i++){
        for(int j=0;j<7-i;j++){
            if(a[j]<a[j+1]){
                float temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
    for(int i=0;i<8;i++){
        printf("%.1f ",a[i]);
    }
    return 0;
}