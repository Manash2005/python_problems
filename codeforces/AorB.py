T = int(input())
for i in range(T):
    X,Y = map(int, input().split())
    A=(500-(X*2))+(1000-(Y+X)*4)
    B=(500-((X+Y)*2))+(1000-Y*4)
    print(max(A,B))