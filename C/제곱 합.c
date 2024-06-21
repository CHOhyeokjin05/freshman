#include <stdio.h>

/*
int main(void){
	
	int i, min, max, sum=0;
	
	scanf("%d %d", &min, &max);
	while (min < max){
		for (i = min; i <= max; i++){
			sum += i*i;
		}
	printf("%d\n",sum);
	scanf("%d %d",&min,&max);
	}	//이중 for문도 가능 
	
	
}*/

int sum(int min, int max);
int main(void){
	int min, max;
	
	scanf("%d %d", &min, &max);
	for (;min < max;){
		printf("%d\n", sum(min, max));
		scanf("%d %d", &min, &max);
	}
	
	
}

int sum(int min, int max){
	int sum = 0, i;
	
	for (i = min; i <= max; i++){
		sum += i*i;
	}
	return sum;
} 
