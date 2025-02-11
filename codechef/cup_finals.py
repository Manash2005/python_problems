# cook your dish here
t = int(input())
for i in range(t):
    X,Y,D = map(int, input().split())
    if(abs(X-Y)<=D):print("YES")
    else:print("NO")