//���������õ��������£�
#include <stdio.h>

//�ж�һ�����Ƿ�Ϊ��ȫ���ĺ���
int        isPerfect(int);

//��ӡ��ȫ���ĺ���
void    printPerfect(int);

int main() {
	int i,a,b,count;

	scanf("%d%d",&a,&b);
	count = 0 ;//a,b��������ȫ������������ʼ��Ϊ0
	for(i=a; i<=b; i++) {
		if (isPerfect(i)) { //�������ȫ��
			printPerfect(i) ;//��ӡ����ȫ��
			count ++ ;  //��������1
		}
	}
	printf("The total number is %d.\n",count);//���a,b��������ȫ��������
	return 0 ;
}

/* ����������д�� */
int isPerfect(int x) {
	int is=0,i,sum=0;
	for(i=1; i<=x/2; i++) {
		if(x%i==0) {
			sum+=i;
		}
	}
	if(sum==x) {
		is=1;
	}
	return is;
}
void    printPerfect(int x) {
	int i,cnt=0;
	printf("%d=",x);
	for(i=1; i<x/2+1; i++) {
		if(x%i==0&&cnt!=0) {
			printf("+%d",i);
		}else if(x%i==0&&cnt==0){
			printf("%d",i);
			cnt++;
		}
	}
	printf("\n");
}
