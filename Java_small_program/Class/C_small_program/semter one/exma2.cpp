#include <stdio.h>
int main(){
int n,m;
long x,y,z;
int cnt;
scanf("%d %d",&n,&m);

for(x=n;x<=m;x++){
	for(y=n;y<=x;y++){
		for(z=n;z<=y;z++){
			
			if((y*y*z*z+x*x*z*z)==(x*x*y*y)){
				cnt++;
			}
		}
	}
}


printf("%d",cnt);



return 0;
}

