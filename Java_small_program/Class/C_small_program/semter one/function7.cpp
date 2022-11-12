//函数被调用的例子如下：
#include <stdio.h>

//判断一个数是否为完全数的函数
int        isPerfect(int);

//打印完全数的函数
void    printPerfect(int);

int main() {
	int i,a,b,count;

	scanf("%d%d",&a,&b);
	count = 0 ;//a,b两数间完全数的数量，初始化为0
	for(i=a; i<=b; i++) {
		if (isPerfect(i)) { //如果是完全数
			printPerfect(i) ;//打印该完全数
			count ++ ;  //计数器加1
		}
	}
	printf("The total number is %d.\n",count);//输出a,b两数间完全数的数量
	return 0 ;
}

/* 请在这里填写答案 */
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
