#include <stdio.h>
int main(void)
{
	int year;
	scanf("%d", &year);
	printf("%.1f", year*3.156e+7);	//0f로 하면 소수점 아래 0번째까지, 즉 소수점 아래 숫자 제거
 } 
