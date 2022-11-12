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
    else return -1 ;//这里两个 return -1 都是无法获得内存时直接结束程序 

    getchar();//吃掉前边输入的回车符 

    for( i = 0 ; i < n ; i++ ) 
        gets(strArray[i]); //读入字符串 

    sort( strArray , n ) ; //排序 
printf("\n");
    for( i = 0 ; i < n ; i++ ) 
        printf("%s\n",strArray[i]); //输出

    for ( i = 0 ; i < n ; i++ )  
        free(strArray[i]) ;
    free(strArray) ;

    return 0;
}

/* 请在这里填写答案 */
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





