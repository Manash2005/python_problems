T = int(input())
for i in range(T):
    A,B,X,Y = map(int, input().split())
    print(A,B,X,Y)
    if A*(1/X) > B*(1/Y):
        print("chefina")
    elif A*(1/X) < B*(1/Y):
        print("chef")
    else:
        print("both")
        