# cook your dish here
T = int(input())
for i in range(T):
    X,Y,Z = map(int,input().split())
    t = Z-(int(Y/X))
    if t>=0:
        print(t)
    else:
        print(0)