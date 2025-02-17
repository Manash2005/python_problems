T = int(input())
for i in range(T):
    X = int(input())
    if X%3==0:
        print("NORMAL")
    elif X%3==1 or X==1:
        print("HUGE")
    else:
        print("SMALL")