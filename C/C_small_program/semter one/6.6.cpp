#include<stdio.h>

void printFactor( int, int );

int main() {
	int a,b,i ;

	scanf( "%d%d", &a, &b );
	for( i = a ; i <= b ; i++ )
		printFactor( i , 1 ) ;

	return 0;
}

/* 请在这里填写答案 */

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
		//	利用i进行输出递归限制
	}
	if(a==1&&i==1) {
		printf("1=1\n");
		i++;
		//	利用i进行输出递归限制
	}
	if(isPrime(a)==1) {
		printf("%d\n",a);
	}
	if(isPrime(a)==0) {

		for(n=2; n<a; n++) {
			if(isPrime(n)==1&&a%n==0) {
				printf("%d*",n);
//				递归一部分 没必要直接递归出答案
//				无返回值 递归算法利用
				printFactor(a/n,i);
//				利用i进行输出递归限制
//				进去后反复 找整除
				break;
//				直接跳出 避免重复
			}
		}
	}


}





