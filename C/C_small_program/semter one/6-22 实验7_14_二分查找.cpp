#include<stdio.h>


//�������ܣ����ֲ���
//�����������ֱ�Ϊ�����ҵ����飬���鳤�ȣ������ҵ�Ԫ��
//��������ֵ������ҵ����򷵻ظ�Ԫ���������е��±꣬���򷵻�-1
int BinarySearch(int a[],int n,int key) ;

int main() {
	int    num[200] ; //�������Ƚϴ��������ĵ������޷�������ô����ڴ棬���С����ԡ�
	int        n , m, i;
	int        key ;

	scanf("%d%d",&n,&m);
	for( i = 0 ; i < n ; i++ )
		scanf("%d",&num[i]) ;

	for( i = 0 ; i < m ; i++ ) {
		scanf("%d",&key) ;
		printf("%d",BinarySearch(num,n,key)) ;
		if ( i != m - 1 ) printf(" ") ;
		else printf("\n") ;
	}
	return 0 ;
}


/* ����������д�� */
int BinarySearch(int a[],int n,int key) {
	int lloc=0,rloc=n-1;
	int Loc=(lloc+rloc)/2;

	while(rloc-lloc!=1&&rloc-lloc!=0) {
		if (key==a[Loc]) {
			return Loc;
		} else if(key>a[Loc]) {
			lloc=Loc;
			Loc=(lloc+rloc)/2;
		} else if(key<a[Loc]) {
			rloc=Loc;
			Loc=(lloc+rloc)/2;
		}

	}
	if(key==a[lloc]) {
		return lloc;
	} else if(key==a[rloc]) {
		return rloc;
	}

	return -1;
}
