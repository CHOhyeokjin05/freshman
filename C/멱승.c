#include <stdio.h>
//��ȯ���� �ֱ� ������ void�� ����ϸ� �� �ȴ�. 
double power(double input, int p);

int main(void)
{
	double input, output;
	int p;
	scanf("%lf %d",&input,&p);
	output = power(input, p);
	printf("%lf",output);	
	
}

//���� ���� 
double power(double input, int p)
{
	double total = 1;
	int i;
	
	for(i=1;i<=p;i++){
		total *= input;
	}
	
	return total;
}
