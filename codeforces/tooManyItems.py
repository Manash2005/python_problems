T = int(input())
for i in range(T):
    N = int(input())
    if(N%10==0):
        print(int(N/10))
    else:
        print(int(N/10)+1)