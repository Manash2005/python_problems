'''Problem Statement: Given two lists of integers, write a program to find their intersection. The intersection of two lists is a new list that contains only the elements that are common to both lists, without duplicates.'''
num_1 = input("Enter numbers separated with spaces:\n")
num_2 = input("Enter numberss separated with spaces:\n")

lst_1 = list(map(float, num_1.split()))
lst_2 = list(map(float, num_2.split()))

lst = []

for i in lst_1:
    for x in lst_2:
        if x == i:
            lst.append(x)
        else:
            continue

print(lst)