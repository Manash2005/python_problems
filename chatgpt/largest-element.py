'''Problem Statement: Given an array of integers, find the second largest element in the array.'''
number = input("Enter number separated spaces: ")
lst = list(map(int,number.split()))
length = len(lst)
print(lst)
greatest_number =-float('inf')
second_greatest_number = -float('inf')
for i in lst:
    if i > greatest_number:
        second_greatest_number = greatest_number
        greatest_number = i
    elif i > second_greatest_number and i != greatest_number:
        second_greatest_number = i
if second_greatest_number == -float('inf'):
    print("There is no second largest number.")
else:
    print("The second largest number is:", second_greatest_number)