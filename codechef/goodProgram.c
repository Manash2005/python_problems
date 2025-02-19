#include <stdio.h>

int main() {
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
	    int X;
	    scanf("%d",&X);
	    if (X%4==0)
	    {
	        printf("Good\n");
	    }
	    else
	    {
	        printf("Not Good\n");
	    }
	}

}

