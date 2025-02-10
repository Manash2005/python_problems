# cook your dish here
T = int(input())
for i in range(T):
    W,X,Y,Z = map(int, input().split())
    if W==X or W==Y or W==Z:
        print("YES")
    elif W==(X+Y) or W==(Z+Y) or W==(Z+X):
        print("YES")
    elif W==(X+Y+Z):
        print("YES")
    else:
        print("NO")