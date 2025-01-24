'''Write a program to classify a given number n as:

"Perfect Number" if the sum of its divisors (excluding itself) equals 𝑛.
"Abundant Number" if the sum of divisors is greater than 𝑛.
"Deficient Number" if the sum of divisors is less than 𝑛.'''

num = int(input("Enter your number: "))
sum = 0
i = 1
while (i < num):
    if (num % i == 0):
        sum += i
    i += 1
if sum == num:
    print(num, "is a Perfect Number.")
elif sum > num:
    print(num, "is an Abundant Number.")
else:
    print(num, "is a Deficient Number.")