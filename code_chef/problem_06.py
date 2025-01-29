# cook your dish here
no_of_test = int((input()))
i = 1
while i <= no_of_test:
    rank = int(input())
    if (1 <= no_of_test <= 100) and (1 <= rank <= 100):
        if rank <= 10:
            print("YES")
        else:
            print("NO")