#find the minimum and maximum of a list
user_input = input("Enter the numbers separated with spaces: ")
num_lst = list(user_input.split())
def integer(x):
    return int(x)
lst = list(map(integer, num_lst))
maximum = max(lst)
minimum = min(lst)

print("Maximum:", maximum)

print("Minimum:", minimum)