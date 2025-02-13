# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    factorial = 1
    if N==0:
        print(factorial)
    else:
        i = N
        while i >=1:
            factorial *= i
            i -= 1
        print(factorial)