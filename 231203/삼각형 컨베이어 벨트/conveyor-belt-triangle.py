n, t = map(int,input().split())
belt = []
for i in range(3) :
    line = list(map(int,input().split()))
    # if i != 0 :
    #     line.reverse()
    belt.append(line)

for a in range(t) :
    arr = [belt[0][n-1],belt[1][n-1],belt[2][n-1]]

    for i in range(3) :
        for j in range(n-1,0,-1) :
            belt[i][j] = belt[i][j-1]
    for i in range(3) :
        if i < 2 :
            belt[i+1][0] = arr[i]
        else :
            belt[0][0] = arr[-1]
for i in range(len(belt)) :
    for j in range(len(belt[i])) :
        print(belt[i][j], end= ' ')
    print()