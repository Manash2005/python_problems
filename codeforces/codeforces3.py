import math
from sympy import isprime
t = int(input())
for i in range(t):
    length = int(input())
    lst = list(map(int,input().split()))
    prime = 0
    for x in lst:
        for y in lst:
            lcm = math.lcm(lst[x-1],lst[y-1])
            if (isprime(lcm)):
                prime += 1
    
    print(prime)