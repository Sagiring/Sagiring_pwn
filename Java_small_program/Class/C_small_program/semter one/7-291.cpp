#include <stdio.h>
int main (){
    int m,n;
    scanf("%d %d",&m,&n);
    int a,b,c,n2,n3,n4;
    n-=m;
    for(a=0;a<=n&&a<=m;a++){
        n2=a;
        
        
    for(b=0;b*2+n2<=n&&b+a<=m;b++){
        n3=b*2;
        
        for(c=0;c*3+n2+n3<=n&&c+a+b<=m;c++){
            n4=n3+n2+c*3;
            if(n4==n){
                printf("%d %d %d\n",a,b,c);
            }
        }
        
    }
    }
    
    
    return 0;
}
