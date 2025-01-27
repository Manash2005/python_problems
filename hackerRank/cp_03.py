#print laast 2 digits of 5 to the power n
n = int(input(""))
if (2 <= n) and (n <= 2*(10**15)) :
    result = 5**n
    digit_2 = (result//10)%10
    digit_1 = result%10
    print(digit_2, digit_1, sep='') 
