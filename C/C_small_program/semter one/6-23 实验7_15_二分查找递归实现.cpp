#include<stdio.h>

#define MAXN 200

int RecurBinarySearch( int a[] , int key , int left , int right ) ;

int main() {
	int        a[MAXN];
	int        n , m , i , key ;

	scanf("%d %d",&n , &m );
	for( i = 0 ; i < n ; i++ )
		scanf("%d", &a[i]);

	for( i =0 ; i < m ; i++ ) {
		scanf("%d",&key);
		printf( "%d" , RecurBinarySearch( a , key , 0 , n - 1 ) );
		if ( i != m - 1 ) printf(" ") ;
		else printf("\n") ;
	}

	return 0;
}

/* 请在这里填写答案 */
int RecurBinarySearch( int a[] , int key , int lloc , int rloc ) {

	int Loc=(lloc+rloc)/2;


	if (key==a[Loc]) {
		return Loc;
	} else if(key>a[Loc]) {
		lloc=Loc;
		Loc=(lloc+rloc)/2;
	} else if(key<a[Loc]) {
		rloc=Loc;
		Loc=(lloc+rloc)/2;
	}

	if(key==a[lloc]) {
		return lloc;
	} else if(key==a[rloc]) {
		return rloc;
	}
		if(rloc-lloc!=1&&rloc-lloc!=0) {
		return	RecurBinarySearch(a,key,lloc,rloc);
	}


	return -1;
}
