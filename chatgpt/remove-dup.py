'''Question:
Write a Python program that takes a space-separated list of integers as input, removes all duplicate values, sorts the remaining numbers in descending order, and then prints the result.'''

nums = input("Enter your numbers separated with spaces:  ")
lst = list(map(int,nums.split()))
print(lst)

lst_2 = set(lst)
print(lst_2)

lst_3 = list(lst_2)
print(lst_3)

lst_3.sort()
print(lst_3)
