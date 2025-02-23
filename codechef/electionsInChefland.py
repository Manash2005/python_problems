# cook your dish here
T = int(input())
for i in range(T):
    N,X = map(int,input().split())
    count = 0
    arr = list(map(int,input().split()))
    for x in arr:
        if x>=X:
            count+=1
    print(count)