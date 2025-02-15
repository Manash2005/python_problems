# cook your dish here
t= int(input())
for i in range(t):
    n = int(input())
    factorial = 1
    if n>0:
        while n>0:
            factorial *= n
            n-=1
        print(factorial)
    else:
        print(0)