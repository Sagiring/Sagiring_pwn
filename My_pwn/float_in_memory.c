#include <stdio.h>

char buf[80];
void vulnerable() {
    int len = -100;
    
    if (len > 80) {
        printf("length too large: bad dog, no cookie for you!");
        return;
    }
    printf("Yes");
    // memcpy(buf, p, len);
}

int main (){
vulnerable();
return 0;
}