#include<stdio.h>
#include<stdlib.h>

char ** create1(int n) ;
void create2( char ** strPtr , int n ) ;
void fill(char ** strPtr , int n) ;


int main() {
	int        n, i;
	char**    strPtr ;

	scanf("%d", &n );
	strPtr = create1( n * 2 + 1 ) ;
	create2( strPtr ,  n * 2 + 1 ) ;
	fill(strPtr , n) ;

	for (i = 0; i < 2 * n + 1; i++) {
		printf("%s\n" , strPtr[i]);
	}

	for ( i = 0 ; i < n * 2 + 1 ; i++ )
		free(strPtr[i]) ;
	free(strPtr) ;

	return 0;
}

char ** create1(int n) {
	char** a;
	a=malloc(sizeof(char*)*n);
	for(int i=0; i<n; i++) {
		a[i]=NULL;
	}
	return a;
}
void create2( char ** strPtr , int n ) {
	for (int i=0; i<n; i++) {
		strPtr[i]=malloc(sizeof(char)*(n+1));
	}
 	for(int i=0; i<n; i++) {
 		for(int cnt=0; cnt<n+1; cnt++) {
 			strPtr[i][cnt]=' ';
 		}
 	}
    	for(int i=0; i<n; i++) {
	int cnt=n;
			strPtr[i][cnt]='\0';
		
	}


}
void fill(char ** strPtr , int n) {

	for(int i=0; i<2*n+1; i++) {
		for(int cnt=0; cnt<2*n+2; cnt++) {
			if((i==0||i==2*n)&&cnt==n) {
				strPtr[i][cnt]='X';
                strPtr[i][cnt+1]='\0';
                
			}
			if((cnt==0||cnt==2*n)&&i==n) {
				strPtr[i][cnt]='X';
                if(cnt==2*n+1){
                    strPtr[i][cnt+1]='\0';
                }
			}
		}
	}
	int i=n,cnt=1;
	while(i>0&&cnt<n) {

		strPtr[i-1][cnt]='/';
		cnt++;
		i--;
	}
	i=n*2,cnt=n+1;
	while(i>0&&cnt<2*n) {

		strPtr[i-1][cnt]='/';
        strPtr[i-1][cnt+1]='\0';
		cnt++;
		i--;
	}
	i=1,cnt=n+1;
		while(i<n&&cnt<2*n) {

		strPtr[i][cnt]='\\';
        strPtr[i][cnt+1]='\0';
            
		cnt++;
		i++;
	}
		i=n+1,cnt=1;
		while(i<2*n&&cnt<n) {

		strPtr[i][cnt]='\\';

		cnt++;
		i++;
	}
}

