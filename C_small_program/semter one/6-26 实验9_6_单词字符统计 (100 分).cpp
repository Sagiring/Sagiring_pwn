
#include<stdio.h>

#define        MAXLEN        110

int        isPrime( int n ) ;//判断一个整数是否是质数，是则返回1，否则返回0 
int        getResult( char word[] ) ;

int main()
{
    char    word[MAXLEN] ;

    scanf( "%s" , word ) ;            
    printf( "%d\n" , getResult( word ) );

    return 0;
}

/* 请在这里填写答案 */
int        isPrime( int n ) {
	for(int i=2;i<n/2+1;i++){
		if(n/i==0){
			return 0;
		}	
		
	}
	return 1;
}
int        getResult( char word[] ) {
//	int cnt;
int max=0,min=0,n,is=0;
//	for(cnt=0;word[cnt]!='\0';cnt++){
////		printf("%d",cnt);
//	}
	for(int i='a';i<='z';i++){
		n=0;
		for(int cnt=0;word[cnt]!='\0';cnt++){
			if(word[cnt]==i){
				n++;
			}
		}
		if(min==0&&n!=0){
			min=n;
		}
		if(n!=0&&n<min){
			min=n;
		}
		if(n>max){
			max=n;
		}
	}
	is=isPrime(max-min);
	if(is!=0){
	
	return (max-min);
}else{
	return -1;
}
}
