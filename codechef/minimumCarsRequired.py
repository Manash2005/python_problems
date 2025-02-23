# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    print(int(N/4) + int(bool(N%4)))