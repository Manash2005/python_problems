'''Problem Statement:

Given two integers L and R, find the sum of all odd numbers between L and R (inclusive).

Input:

Two integers L and R where 1 ≤ L ≤ R ≤ 10^6.
Output:

The sum of all odd numbers between L and R (inclusive).'''

L = int(input("Enter the value of L: "))

R = int(input("Enter the value of R: "))
sum = 0
if (1 <= L <= R <= 10**6):
    if L%2 != 0:
        i = L
        while(i <= R):
            sum += i
            i += 2
    else:
        i = L+1
        while(i <= R):
            sum += i
            i += 2        
else:
    print("invalid input")

print(f"The sum is {sum}")
