T = int(input())
for i in range(T):
    N = int(input())
    deck = None
    seat = None
    if(N<=15):
        deck = "Lower"
        if(N<=10):
            seat = "Double"
        else:
            seat="Single"
    else:
        deck = "Lower"
        if(N<=25):
            seat = "Double"
        else:
            seat="Single"

    print(f"{deck} {seat}")