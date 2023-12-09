n, m, k = map(int,input().split())
board = []
for i in range(n) :
    line = list(map(int,input().split()))
    board.append(line)
k -= 1

dx = [1,0]

def check(x,y) :
    nx = x + 1
    ny = y
    flag = False
    if 0 <= nx < n and 0 <= ny < n :
        if board[nx][ny] == 1 :
            flag = True
            return flag
        else :
            return flag
    return flag

for i in range(n) :
    total_flag = False
    for j in range(k,k+m) :
        result = check(i,j)
        if result :
            total_flag = True
            board[i][k:k+m] = [1] * m
            break
    if total_flag :
        break
for i in range(len(board)) :
    for j in range(len(board[i])) :
        print(board[i][j], end=' ')
    print()