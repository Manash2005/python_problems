#include <stdio.h>

int main() {
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
    {
        int X;
        scanf("%d",&X);
        if (X<=50)
        {
            printf("LEFT\n");
        }
        else
        {
            printf("RIGTH\n");
        }
    }

}

