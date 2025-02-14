n = int(input())
x = 0
i = 1
while i<=n:
    inp = input()
    if inp == "++X" or inp == "X++":
        x += 1
    else:
        x -= 1
    i+=1
print(x)