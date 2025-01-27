num_1 = int(input(""))
num_2 = int(input(""))
num_3 = int(input(""))

if 1 <= num_1 <= 10 and 1 <= num_2 <= 10 and 1 <= num_3 <= 10:
    results = [
        num_1 + num_2 + num_3,
        num_1 * num_2 * num_3,
        (num_1 + num_2) * num_3,
        num_1 * (num_2 + num_3)
    ]
    max_result = max(results)
    print(max_result)
