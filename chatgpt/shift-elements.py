num = input("Enter your number separated with spaces: ")
lst = list(map(int,num.split()))
print(lst)

n = len(lst)
lst_2 = lst[(n-1)::] + lst[:(n-1):]
print(lst_2)