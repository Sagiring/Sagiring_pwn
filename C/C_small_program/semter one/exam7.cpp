//#include <stdio.h>
//int main(){
//int n,i,cnt=1;
//long long result=1,mu=1;
//
//
//scanf("%d",&n);
//if(n==0){
//	printf("%lld",result);
//}else{
//
//for(i=n+1;i<=2*n;i++){
//	
//	
//result=i*result;
//
//if(cnt<=n/2+1){
//	result=result/(cnt*(cnt+1));
//	cnt++;
//}
//
//}
//
//result=result/cnt;
//
//printf("%lld",result);
//
//
//}
//
//return 0;
//}
#include<stdio.h>
long long f(int n)
{
 if(n==1||n==0)
 {
  return 1;
 }
 else
 {
  return f(n-1)*(4*n-2)/(n+1);
 }
}
int main(void)
{
 int n;
 scanf("%d",&n);
 printf("%lld",f(n));
 return 0;

}
