#include <stdio.h>
int main(void){
	char ch;
	
	scanf("%c",&ch);
	for (ch = '$';ch != 'g';scanf("%c",&ch)){
		putchar(ch);
	}

	
	int k;
	for (k = 1, printf("%d: 안녕!\n",k); printf("k = %d\n",k), k*k < 26; k += 2, printf("이제 k는 %d\n",k) ){
		printf("루프 몸체에서 k는 %d\n",k);
	}
	//initialize, check, execute, update => 가장 나중에 "이제 ~" 출력됨. 
}
