# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    remove = 0
    arr = list(map(int,input().split()))
    for x in arr:
        if x>=1000:
            remove += 1
    print(remove)