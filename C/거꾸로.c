#include <stdio.h>
#include <string.h>

int main(void){
	
	char var[40];
	int index;
	
	scanf("%s", var);
	index = strlen(var)-1;
	printf("%d",index);
}
