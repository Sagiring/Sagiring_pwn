#include <stdio.h>
#define LINES 12

main()
{
int line;
int count; // �������� ���ڼ�¼ÿ����Ҫ��ӡ�ġ�*������
line=1;
while (line<=LINES){
//�����line��:���line��*��
count=1;
while(count<=line) {
printf("*");//�����count��* 
count = count+1;
}
printf("\n"); 
line=line+1; 
}

return 0;
}

