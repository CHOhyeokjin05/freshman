#include <stdio.h>
#define PRAISE "You are an extraordinary being." 

int main(void)
{
	char name[40];
	
	printf("실례지만  성함이 어떻게 되시는지?\n");
	scanf("%s",name);   //배열은 name 이 자체가 주소 
	printf("반갑습니다, %s 씨. %s\n",name,PRAISE);
}
