T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    Y = N-X
    print(min(X,Y))