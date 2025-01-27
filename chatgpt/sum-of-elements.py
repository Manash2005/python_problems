#sum of elements in the list
lst = []
sum = 0 
while True:
    num = int(input("Enter your nummber: "))
    lst.append(num)
    consent = input("Do you want to add more numbers? (y/n): ")
    if consent.lower() != 'y':
        break

for i in lst:
    sum += i
print(lst)
print(f"Sum of elements in the list is: {sum}")