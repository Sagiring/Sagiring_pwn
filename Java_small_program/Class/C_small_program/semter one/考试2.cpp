#include <stdio.h>
int main(){
int n,score,win,lost;
scanf("%d",&n);
for(;n>0;n--){
	scanf("%d %d",&win,&lost);
	if(win>lost){
		score+=3;
	}else if(win==lost){
		score++;
	}else if(win<lost){
		score=score;
	}
}


printf("%d",score);

return 0;
}

