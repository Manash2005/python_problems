t = int(input())

while t > 0:
    n = int(input()) #length of the binary
    s = input()# binary string
    A = "00"
    T = "01"
    C = "10"
    D = "11"
    arr=[]
    for i in range(0,n,2):
        x = s[i:i+2]
        arr.append(x)
    for i in arr:
        if i =="00":
            print("A",end='')
        elif i == "01":
            print("T",end='')
        elif i == "10":
            print("C",end='')
        else:
            print("G",end='')
    print("")
    t -= 1
