#include<stdio.h>
int main()
{
int i;
float f;
char c;

printf("input i,f\n");

scanf("%d,%f", &i,&f );

getchar(); 

printf("input c\n");

scanf("%c", &c );
printf("the result is:\n"); 
printf("i=%d,f=%f,c=%c",i,f,c);


return 0;
}
