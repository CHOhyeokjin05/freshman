#include <stdio.h>
int main(void)
{
	unsigned width, precision;
	int number = 256, n;
	double weight = 242.5;
	
	printf("�ʵ� �ʺ� �Է��Ͻÿ�:\n");
	scanf("%d",&width);
	printf("Number:%*d:\n",width,number);   //*������
	
	scanf("%*d %*d %d", &n);   //*������ 
	printf("%d",n);
 } 
