#include <stdio.h>
int main(){
   int a,b,c,d,e;//���ڼ�¼A��E�ֱ������ 
   int countA,countB,countC,countD,countE;//���ڼ�¼A��E�ֱ�˵�ԵĻ����� 
   
   for(a=1;a<=5;a++)//a��e�ֱ����A��Eѡ�ֵ����� 
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
        		              printf("����������:\n"); 
        		              printf("A:��%d��\nB:��%d��\nC:��%d��\nD:��%d��\nE:��%d��\n",a,b,c,d,e);
                                               } //if
                                               
                                               return 0;
} 
