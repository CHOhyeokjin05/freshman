#include <stdio.h>
int main(void){
	int i, j;
	char al;
	
	for (i = 1; i <= 5; i++){
		for (j = 5-i; j >= 1; j--){
			printf(" ");
		}
		for (al = 'A'; al < (char) ((int) 'A'+i); al++){
			printf("%c",al);
		}
		for (al-2; al-2 >= 'A'; al--){
			printf("%c", al-2);
		}
		printf("\n");
	}
	printf("\n");
	printf("%d", (int) 'A'+1);
	printf("%c", (char) ((int) 'A'+1));
	printf("%c", (char) (int) 'A'+1);	//int 수행, char 수행, 합산 
}
