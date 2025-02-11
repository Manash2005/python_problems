T = int(input())
S = []
for i in range(T):
    s = input()
    S.append(s)
for x in S:
    if len(x)>10:
        print(x[0]+str(len(x)-2)+x[-1])
    else:
        print(x)