#include <stdio.h>
#define size 8
int main(void)
{
	double a[size], b[size];
	int i, j;
	// 8�� �Է� �ޱ� 
	for (i=0; i < size; i++)
	{
		scanf("%lf", &a[i]);
	}
	// b�� �ε��� �ϸ鼭 ���ϴ� �� ����ֱ� 
	for (i=0; i < size; i++)
	{
		for (j=0; j <= i; j++)
		{
			b[i] += a[j];
		}
	}
	//printf
	for (i=0; i < size; i++){
		printf("%3.1lf, %3.1lf ", a[i], b[i]);
	}	
	
}
