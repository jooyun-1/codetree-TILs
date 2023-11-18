n, t = map(int,input().split())
belt = []
for i in range(2) :
    line = list(map(int,input().split()))
    if i == 1 :
        line.reverse()
    belt.append(line)
for k in range(t) :
    temp = belt[0][n-1]
    temp2 = belt[1][0]
    for i in range(n-1,0,-1) :
        belt[0][i] = belt[0][i-1]
    belt[0][0] = temp2

    for i in range(n-1) :
        belt[1][i] = belt[1][i+1]

    belt[1][n-1] = temp

for i in range(2) :
    if i == 1 :
        belt[i].reverse()
    for j in range(n) :
        print(belt[i][j], end=" ")
    print()