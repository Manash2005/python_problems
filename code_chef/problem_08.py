# cook your dish here
T = int(input())
if 1<=T<=6:
    i = 1
    while i<=T:
        X = int(input())
        if 1 <= X <= 6:
            if X == 6:
                print("YES")
            elif 1 <= X < 6:
                print("NO")
        
        i += 1