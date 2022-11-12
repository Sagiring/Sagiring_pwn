#include <stdio.h>


int    evaluation(int n,int a) ;
int main()
{
       int        n , a ; 

       scanf("%d%d",&n,&a);       
       printf("%d\n",evaluation(n,a));

    return 0;
}

/* 请在这里填写答案 */
int    evaluation(int n,int a) {
	int i,sum=1;
	
	if(n+1==0){
		return 1;
	}else{
		for(i=n+1;i>0;i--){
			sum*=a;
		}
	return evaluation(n-1,a)+sum;
	}
}
