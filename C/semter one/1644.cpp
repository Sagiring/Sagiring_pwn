#include <stdio.h>
int main(){
	char a,b,c;
	int a1=0,b1=0,c1=0;
	scanf("%c%c%c",&a,&b,&c);
	
    a1=a;
    b1=b;
    c1=c;
    if((a>='a'&&a<='z')||(a>='A'&&a<='Z')||(b>='a'&&b<='z')||(b>='A'&&b<='Z')||(c>='a'&&c<='z')||(c>='A'&&c<='Z')){
	
    if(a1+1==b1){
    	if(b1+1==c1){
    		printf("Yes");
		}else{
			printf("No");
		}
	}else{printf("No");
	}
}else{
	printf("No");
}

	
	
//	printf("%d %d %d",a1,b1,c1);
	
	
	
	return 0;
}
