#include <stdio.h>
#include <string.h>

int main(void)
{
	char first[10], second[10];
	scanf("%s",&first);
	scanf("%s",&second);
	
	printf("%s %9s\n%7d %9d",first,second,strlen(first),strlen(second));
	printf("\n%s %s\n%d %7d",first,second,strlen(first),strlen(second));
}
