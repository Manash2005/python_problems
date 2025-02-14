A,B,C,X = map(int,input().split())
arr =[A,B,C]
flag = 0
for i in arr:
    if i == X:
        print("YES")
        flag = 1
        break
if flag==0:
    print("NO")