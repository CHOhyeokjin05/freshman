#include <stdio.h>
int main(void)
{
	int n = 30;
	int v;
	
	double x = 2.33e+002;
	
	v = printf("%d",n);
	
	printf("\n%d\n",v);
	printf("%*d",v,n);
	printf("\n%12.2e",x);
 } 
