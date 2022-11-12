#include <stdio.h>

int main() {
	int n;
	long long An=0,Sn=0;
	scanf("%d",&n);
	if(n==1||n==2) {
		printf("0");
	} else {
for(int cnt=3;cnt<=n;cnt++){
		An+=1ll*(cnt-2)*(cnt-1)*cnt;
		Sn+=An;
		
	}
	printf("%lld",Sn);
}
return 0;
}
