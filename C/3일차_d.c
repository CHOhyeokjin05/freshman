#include <stdio.h>
int main(void){
	char ch;
	
	scanf("%c",&ch);
	for (ch = '$';ch != 'g';scanf("%c",&ch)){
		putchar(ch);
	}

	
	int k;
	for (k = 1, printf("%d: �ȳ�!\n",k); printf("k = %d\n",k), k*k < 26; k += 2, printf("���� k�� %d\n",k) ){
		printf("���� ��ü���� k�� %d\n",k);
	}
	//initialize, check, execute, update => ���� ���߿� "���� ~" ��µ�. 
}
