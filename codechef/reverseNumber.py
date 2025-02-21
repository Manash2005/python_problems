T = int(input())
for i in range(T):
    N = input()
    while int(N)%10==0:
        N=str(int(N)//10)
    print(N[::-1])
        
    
    