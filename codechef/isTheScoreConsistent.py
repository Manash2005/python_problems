T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    C,D = map(int, input().split())
    if (A<=C) and (B<=D):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")