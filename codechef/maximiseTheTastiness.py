T = int(input())
for i in range(T):
    a,b,c,d = map(int,input().split())
    print((max(a,b)+(max(c,d))))