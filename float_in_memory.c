#include <stdio.h>
int main (){
    float a=11.28125;
    char *p =(char *)&a ;
    

    for(int i=0;i<8;i++){
printf("%x ",*(char *)(p+i));
    }
    
    
return 0;
}