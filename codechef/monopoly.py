T = int(input())
for i in range(T):
    P,Q,R,S = map(int,input().split())
    arr = [P,Q,R,S]
    sum = 0
    flag = 0
    for i in arr:
        sum += i
    for i in arr:
        if i > (sum-i):
            print("YES")
            flag = 1
            break
    if flag == 0:
        print("NO")
