T = int(input())
for i in range(T):
    A,B,C = map(int,input().split())
    
T = int(input())
for i in range(T):
    A,B,C = map(int,input().split())
    if A>=C:
        if B>=A:
            print("YES")
        else:
            print("NO")
    else:
        if B>=C:
            print("YES")
        else:
            print("NO")