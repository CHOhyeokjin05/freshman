#include <stdio.h>
#define SIZE 10
#define PAR 72
int main(void)
{
	int index, score[SIZE];
	int sum = 0;
	float average;
	
	printf("%d���� ���� ���ھ �Է��Ͻÿ�:\n",SIZE);
	for (index = 0; index < SIZE; index++){
		scanf("%d", &score[index]);
		
	}
	printf("���� ���ھ���� ������ ����:\n");
	for (index = 0; index < SIZE; index++){
		printf("%5d", score[index]);
		
	}
	printf("\n");
	for (index = 0; index < SIZE; index++){
		sum += score[index];
	}
	average = (float) sum / SIZE;
	printf("���ھ��� �� = %d, ��� = %.2f\n", sum, average);
	printf("�ڵ�ĸ�� %.0f",average-PAR);
	
	return 0;
}