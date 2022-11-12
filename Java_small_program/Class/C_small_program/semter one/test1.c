#include <stdio.h>

int main(){
	int cm;
	int inch,foot;
	
	scanf("%d",&cm);
	inch=cm/30.48*12;
	foot=inch/12;
	inch=inch-foot*12;
	

	
	printf("%d %d",foot,inch);
	
	
	
	
	
	return 0;
}
