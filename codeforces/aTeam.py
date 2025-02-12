n = int(input())
arr = []
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
for i in arr:
    agree = 0
    for x in i:
        if x == 1:
            agree += 1
    if agree>=2:
        ans +=1
print(ans)