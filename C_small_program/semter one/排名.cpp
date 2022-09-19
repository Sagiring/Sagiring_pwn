#include <stdio.h>
int main(){
   int a,b,c,d,e;//用于记录A～E分别的名次 
   int countA,countB,countC,countD,countE;//用于记录A～E分别说对的话个数 
   
   for(a=1;a<=5;a++)//a～e分别代表A～E选手的名次 
	   for(b=1;b<=5;b++)
	       if (a!=b)
                  for(c=1;c<=5;c++)	
		       if (c!=a &&c!=b)
		           for(d=1;d<=5;d++)		 		
		               if (d!=a && d!=b && d!=c)
		                  for(e=1;e<=5;e++)	
    	   	                     if (e!=a && e!=b && e!=c && e!=d)
    	 	                       if ((b==2 && a!=3 || b!=2 && a==3) &&
                                                    (b==2 && e!=4 || b!=2 && e==4) &&
                                                    (c==1 && d!=2 || c!=1 && d==2) &&
                                                    (c==5 && d!=3 || c!=5 && d==3) &&
                                                    (e==4 && a!=1 || e!=4 && a==1)) { 
        		              printf("比赛名次是:\n"); 
        		              printf("A:第%d名\nB:第%d名\nC:第%d名\nD:第%d名\nE:第%d名\n",a,b,c,d,e);
                                               } //if
                                               
                                               return 0;
} 
