distance = int(input(""))
distance_day = distance * 2
distance_week = distance_day * 5

if 1 <= distance <= 10**8:
    print(distance_week)
else:
    print("")