# cook your dish here
T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    if N>M:
        print((N-M)*2 + M)
    else:
        print(N)
        