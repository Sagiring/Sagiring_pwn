#include<stdio.h>

void printFactor( int, int );

int main() {
	int a,b,i ;

	scanf( "%d%d", &a, &b );
	for( i = a ; i <= b ; i++ )
		printFactor( i , 1 ) ;

	return 0;
}

/* ����������д�� */

int isPrime(int n) {
	int i=2,isPrime=1;
	if(n!=1) {

		for(i=2; i<n/2+1; i++) {

			if(n%i==0) {
				isPrime=0;
				break;
			}
		}
		return isPrime;
	}
}

void printFactor( int a, int i) {
	int n;

	if(a!=1&&i==1) {
		printf("%d=",a);
		i++;
		//	����i��������ݹ�����
	}
	if(a==1&&i==1) {
		printf("1=1\n");
		i++;
		//	����i��������ݹ�����
	}
	if(isPrime(a)==1) {
		printf("%d\n",a);
	}
	if(isPrime(a)==0) {

		for(n=2; n<a; n++) {
			if(isPrime(n)==1&&a%n==0) {
				printf("%d*",n);
//				�ݹ�һ���� û��Ҫֱ�ӵݹ����
//				�޷���ֵ �ݹ��㷨����
				printFactor(a/n,i);
//				����i��������ݹ�����
//				��ȥ�󷴸� ������
				break;
//				ֱ������ �����ظ�
			}
		}
	}


}





