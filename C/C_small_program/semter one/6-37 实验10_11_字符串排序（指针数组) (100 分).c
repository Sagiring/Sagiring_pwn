#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define        MAX        101

char **    create1( int n ) ;
char *    create2( int n ) ;
void    sort( char** strArray , int size ) ; 

int main()
{
    char**    strArray ;
    int        n , i ;

    scanf("%d",&n) ;
    strArray = create1( n ) ; 
    if ( strArray != NULL ) 
    {
        for ( i = 0 ; i < n ; i++ ) 
        {
            strArray[i] = create2( MAX ) ;
            if ( strArray[i] == NULL ) return -1 ;
        }            
    }
    else return -1 ;//�������� return -1 �����޷�����ڴ�ʱֱ�ӽ������� 

    getchar();//�Ե�ǰ������Ļس��� 

    for( i = 0 ; i < n ; i++ ) 
        gets(strArray[i]); //�����ַ��� 

    sort( strArray , n ) ; //���� 
printf("\n");
    for( i = 0 ; i < n ; i++ ) 
        printf("%s\n",strArray[i]); //���

    for ( i = 0 ; i < n ; i++ )  
        free(strArray[i]) ;
    free(strArray) ;

    return 0;
}

/* ����������д�� */
char **    create1( int n ) {
	char **p=NULL;
	p=malloc(sizeof(char*)*n);
	return p;
}
char *    create2( int n ) {
	char *p;
	for(int i=0;i<n;i++){
		p=malloc(sizeof(char)*n);
	}
	return p;
}
void    sort( char** strArray , int size ) {
	int is;
	char c[size];
	for(int cnt=1;cnt<size;cnt++){
	
	for(int i=0;i<size-cnt;i++){
	is=strcmp(strArray[i],strArray[i+1]);
	if(is>0){
		strcpy(c,strArray[i]);
		strcpy(strArray[i],strArray[i+1]);
		strcpy(strArray[i+1],c);
	}
}

}
}





