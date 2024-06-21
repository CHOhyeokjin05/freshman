#include <stdio.h>

double cal(double n, double m);
int main(void){
	double n, m, res;

	/*
	scanf("%lf %lf", &a, &b);
	for (a,b; ; scanf("%lf %lf", &a, &b) ){
		printf("%lf\n",(a-b)/(a*b));
	}*/
	
	//scanf가 성공적으로 스캔한 개수 == 2 
	while (scanf("%lf %lf", &n, &m) == 2){
 		res = (n - m) / (n * m);
 		printf("(%.3g - %.3g)/(%.3g*%.3g) = %.5g\n", n, m, n, m, res);
 		printf("%.5g\n", cal(n,m));
 		printf("Enter next pair (non-numeric to quit): ");
 	}
	
	
}

double cal(double n, double m){
	double res;
	
	res = (n-m)/(n*m);
	
	return res;
} 
