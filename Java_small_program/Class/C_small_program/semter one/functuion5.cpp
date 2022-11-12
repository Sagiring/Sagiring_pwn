//函数被调用的例子如下：
#include<stdio.h>

int mypow(int , int ) ;

int main()
{
    int x, n ;

    scanf("%d%d",&x,&n) ;
    printf("%d\n",mypow(x,n)) ;

    return 0;
}

/* 请在这里填写答案 */
int mypow(int x, int n) {
	int y,n1;
	n1=n;
	for (y=1;n1!=0&&x!=0;n1--){
		y=y*x;
	}
	
	if(n==0&&x!=0){
		y=1;
	}else if(x==0){
		y=0;
	}
	
	
	
	
	return y;
}
