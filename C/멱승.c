#include <stdio.h>
//반환값이 있기 때문에 void를 사용하면 안 된다. 
double power(double input, int p);

int main(void)
{
	double input, output;
	int p;
	scanf("%lf %d",&input,&p);
	output = power(input, p);
	printf("%lf",output);	
	
}

//이하 동문 
double power(double input, int p)
{
	double total = 1;
	int i;
	
	for(i=1;i<=p;i++){
		total *= input;
	}
	
	return total;
}
