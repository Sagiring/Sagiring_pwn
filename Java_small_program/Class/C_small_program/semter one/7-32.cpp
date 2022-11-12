#include <stdio.h>


int main(){
int n,qie=2;
scanf("%d",&n);
if(n==0){
	qie=1;
}
for(int i=2;i<=n;i++){
	qie+=i;
}

printf("%d",qie);


return 0;
}

