# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    arr = []
    x = 0
    while x<N:
        if S[x]=='A':
            arr.append('T')
        elif S[x]=='T':
            arr.append('A')
        elif S[x]=='C':
            arr.append('G')
        elif S[x]=='G':
            arr.append('C')
        x+=1
    print("".join(arr))
        