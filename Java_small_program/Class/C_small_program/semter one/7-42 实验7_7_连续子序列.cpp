#include <stdio.h>
int main() {
	int a[1000];
	int b[1000];
	int is=2,geb,gea;
	for(int i=0;; i++) {
		scanf("%d",&a[i]);
		if(a[i]==-1) {
			gea=i;
			break;
		}
	}
	for(int i=0;; i++) {
		scanf("%d",&b[i]);
		if(b[i]==-1) {
			geb=i;
			break;
		}
	}
	for(int cnt; cnt<geb; cnt++) {
		for(int i=0; i<gea; i++) {
			if(b[cnt]==a[i]&&geb!=1) {
				for(int x=1; x<geb; x++) {
					if(b[cnt+x]!=a[i+x]) {
						is=0;
						break;
					}
				}
			}else if(b[cnt]==a[i]&&geb==1){
				is=1;
			}
			if(i==gea-1||is==0) {
				is=0;
				break;
			}
		}
		if(is==0) {
			break;
		}
		if((is==2&&cnt==geb-1)||is==1) {
			is=1;
		}
	}

	if(is==1) {
		printf("ListB is the sub sequence of ListA.");
	} else if(is==0) {
		printf("ListB is not the sub sequence of ListA.");
	}




	return 0;
}

