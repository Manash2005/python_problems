T = int(input())
for i in range(T):
    N,X,Y = map(int,input().split())
    if Y%X == 0:
        print("YES") 