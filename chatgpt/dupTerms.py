'''Write a Python program to find the common elements between two lists, but only include the elements that appear in both lists exactly once (i.e., ignore duplicates).'''

num = input("Enter your number separated with spaces: ")
lst = list(map(int, num.split()))
print(lst)
for x in lst:
    i =  