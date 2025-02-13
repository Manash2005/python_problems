T = int(input())
for i in range(T):
    X,Y,R = map(int,input().split()) #x is limit,Y is sticks/plate,R is rupees
    extra = R/30
    total = X + extra
    if total%Y == 0:
        print(int(total/Y))
    else:
        print(int(total/Y)+1)
