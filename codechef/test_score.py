# cook your dish here
T = int(input())
for i in range(T):
    N,X,Y = map(int,input().split())
    if Y % X == 0 and (0 <= Y // X <= N): 
        print("YES")
    else:
        print("NO")
        