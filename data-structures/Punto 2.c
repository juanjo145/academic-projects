#include<stdio.h>
#include <math.h>
int main(){
	int n,casos,x,b,i=0;
	char arr1[5000] ;
	scanf("%d",&casos);
	for (i=0 ; i<casos ; i++ )
		scanf("%d",&n); 
		x = pow(66,n);
		b = x%100;
	    arr1[i] = arr1[b];
	for(i=0 ; i<casos ; i++)
		printf("%c \n",arr1[i]);
	return 0 ;
	
}
