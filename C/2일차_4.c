#include <stdio.h>
int main(void){
	int i, j, list[11];	//list[10]���� �ϸ� �޸� ħ�� �Ͼ 
	
	for (i = 1; i <= 10; i++){
		list[i] = 2*i + 3;
		for (j = 1; j <= i; j++){
			printf(" %d", list[j]);
		}
		printf("\n");
	}
	
}
