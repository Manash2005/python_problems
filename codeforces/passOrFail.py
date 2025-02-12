T = int(input())
for i in range(T):
    N,X,P = map(int, input().split())
    marks = 3*X + (N-X)*-1
    if marks>=P:
        print("PASS")
    else:
        print("FAIL")