# cook your dish here
T = int(input())
for i in range(T):
    X, N = map(int, input().split())
    points_per_problem = int(X/10)
    print(points_per_problem*N)