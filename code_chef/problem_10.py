# cook your dish here
inp = input()
lst = list(map(int, inp.split()))
X = lst[0]
Y = lst[1]
if 1<= Y <= X <= 1000:
    problems_left = X - Y

print(problems_left)