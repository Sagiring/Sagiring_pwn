#include <stdio.h>
#define LINES 12

main()
{
int line;
int count; // 计数器， 用于记录每行需要打印的‘*’个数
line=1;
while (line<=LINES){
//输出第line行:输出line个*号
count=1;
while(count<=line) {
printf("*");//输出第count个* 
count = count+1;
}
printf("\n"); 
line=line+1; 
}

return 0;
}

