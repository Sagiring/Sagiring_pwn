#include <stdio.h>

int main(){
	
	double pi,off,a;
    scanf("%lf",&off);
    pi=1;
    a=1;
    int n=1,cnt=n;
    while(a>off){
    	a=1;
    	while(cnt>=1){
		a*=cnt/(2*cnt+1.0);
		cnt--;
//		printf("a=%f\n",a);
    }
    	pi+=a;
    	
    	n++;
//    	printf("pi=%f\n",pi);
    	cnt=n;
    	
    	
    	
    	
	}
	printf("%.6f",pi*2);
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}
