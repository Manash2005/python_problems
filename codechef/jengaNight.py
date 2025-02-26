T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    if X%N == 0:
        print("YES")
    else:
        print("NO")