# cook your dish here
T = int(input())
for i in range(T):
    N = int(input()) # days left for halloween
    weeks = int(N/7)
    extra = N%7
    tuesdays = weeks
    if extra>=2:
        tuesdays += 1
    print(tuesdays)