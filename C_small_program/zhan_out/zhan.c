#include <stdio.h>


int main(){

int modified=0;
char buffer[12];

gets(buffer);//这里发生栈溢出

if (modified==0){
    printf("Try again");
}else{
    printf("You have success");

}
    return 0;
}