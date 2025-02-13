T = int(input())
for i in range(T):
    X,Y,A,B = map(int,input().split())
    arr = [X,Y,A,B]
    arr = list(set(arr))
    print(len(arr)-2)