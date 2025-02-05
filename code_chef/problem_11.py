# cook your dish here
T = int(input())
if 1<=T<=100:
    inp = input()
    lst = list(map(int, inp.split()))
    X = lst[0]  #Total points for the problem
    N = lst[1]  #The number of test cases passed
    i = 1
    if (10<=X<=200) and (0<=N<=10) and (X%10==0):
        while (i<=T):
            points_per_problem = X/10
            score = points_per_problem * N
            print(score)
            i += 1
        
        
