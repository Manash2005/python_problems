#include <stdio.h>

int main() {
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
	    int A,B;
	    scanf("%d",&A);
	    scanf("%d",&B);
	    int C = A*10;
	    int D = B*5;
	    if (C>D)
	    {
	        printf("FIRST\n");
	    }
	    else if(D>C)
	    {
	        printf("SECOND\n");
	    }
	    else
	    {
	        printf("ANY\n");
	    }
	}

}

