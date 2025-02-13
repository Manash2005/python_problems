R,O,C = map(int, input().split()) 
runs_left = R - C
overs_left = 20 - O
maximum = C + 6*6*overs_left
if maximum>R:
    print("YES")
else:
    print("NO")
