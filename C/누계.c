#include <stdio.h>
#define size 8
int main(void)
{
	double a[size], b[size];
	int i, j;
	// 8개 입력 받기 
	for (i=0; i < size; i++)
	{
		scanf("%lf", &a[i]);
	}
	// b를 인덱싱 하면서 원하는 값 집어넣기 
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
