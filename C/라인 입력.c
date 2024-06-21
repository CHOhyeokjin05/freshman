#include <stdio.h>
#include <string.h>

int main(void){
	char line[255];
	int i=0;
	

	/*
	for (i=0; i < 255; i++)
	{
		scanf("%c", &line[i]);
	}
	
	for (i=strlen(line)-1; i>=0;i--)
	{
		printf("%c", line[i]);
	} Á¤Áö°¡ ¾È µÊ.*/ 
	printf("Enter a line to reverse:\n");
	while (scanf("%c", &line[i]), line[i] != '\n')
		i++;

	for (; 0 <= i; i--) // previous loop leaves i in right position
		printf("%c", line[i]);

	printf("\n");

	return 0;

}
