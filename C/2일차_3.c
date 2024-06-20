#include <stdio.h>
int main(void)
{
	unsigned width, precision;
	int number = 256, n;
	double weight = 242.5;
	
	printf("필드 너비를 입력하시오:\n");
	scanf("%d",&width);
	printf("Number:%*d:\n",width,number);   //*변경자
	
	scanf("%*d %*d %d", &n);   //*변경자 
	printf("%d",n);
 } 
