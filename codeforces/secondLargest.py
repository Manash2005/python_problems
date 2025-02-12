T = int(input())
for i in range(T):
    largest = -float('inf')
    second_largest = -float('inf')
    arr = list(map(int, input().split()))
    for x in arr:
        if x>=largest:
            second_largest = largest
            largest = x
        elif x!=largest and x>second_largest:
            second_largest = x
    print(second_largest)