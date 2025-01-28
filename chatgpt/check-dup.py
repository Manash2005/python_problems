'''Write a Python program that checks if a given list contains any duplicates. If there are duplicates, remove them and print the updated list.'''

num = input("Enter your number: ")
lst = list(map(int,num.split()))
print(lst)
lst_2 = list(set(lst))

if lst == lst_2:
    print("There are no duplicates in the list")
else:
    print(lst_2)