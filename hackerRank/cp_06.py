n = int(input(""))
if (1 <= n <= (10**9) + 10):
    if n < 2:
        print("nonprime")
    else:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print("prime")
        else:
            print("nonprime")
else:
    print("")