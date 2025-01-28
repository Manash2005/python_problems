'''Write a Python program that takes a list of numbers as input and performs the following operations:

Find and print the largest and smallest numbers in the list.
Remove all occurrences of the smallest number from the list.
Print the updated list.'''

nums = input("Enter your number separated with spaces: ")
lst = list(map(int,nums.split()))
max_lst = max(lst)
min_lst = min(lst)

for num in lst:
    if num == min_lst:
        lst.remove(num)
    else:
        continue

print(min_lst)
print(max_lst)
print(lst)