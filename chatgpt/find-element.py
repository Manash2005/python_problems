'''Problem Statement:
Given a list of integers and a target integer, find all the indices where the target integer appears in the list.'''

nums = input("Enter your numbers separated by spaces: ")
lst = list(map(float, nums.split()))
integer = int(input("Enter your numbr you want to find: "))

i = 0
for num in lst:
    if num == integer:
        print(i)
    i += 1
    
