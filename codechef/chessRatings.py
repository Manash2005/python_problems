# cook your dish here
T = int(input())
for i in range(T):
    X,Y = map(int,input().split())
    if (Y-X)%8 == 0:
        print(int((Y-X)/8))
    else:
        print(int((Y-X)/8)+1)
        