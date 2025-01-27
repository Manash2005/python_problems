n = int(input(""))  # number of toys
lst_of_toys = input("").split()  # labelling of toys separated by spaces starting from 0
if (1 <= n <= 100) and (0 <= len(lst_of_toys) <= 100):
    lst_of_toys = [int(toy) for toy in lst_of_toys]
    all_toys = set(range(n))
    missing_toy = all_toys - set(lst_of_toys)
    print(missing_toy.pop())