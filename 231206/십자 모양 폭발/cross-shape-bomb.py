n = int(input())
board = []
for i in range(n) :
    line = list(map(int,input().split()))
    board.append(line)
r, c = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
r -= 1
c -= 1
def bomb(x,y,num) :
    first_x = x
    first_y = y
    board[x][y] = 0
    for i in range(4) :
        for j in range(num-1) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                board[nx][ny] = 0
                x = nx
                y = ny
        x = first_x
        y = first_y
bomb(r,c,board[r][c])

temp_arr = [[0]*n for _ in range(n)]

for j in range(n) :
    row = n-1
    for i in range(n-1,-1,-1) :
        if board[i][j] != 0 :
            temp_arr[row][j] = board[i][j]
            row -= 1
for i in range(n) :
    for j in range(n) :
        print(temp_arr[i][j], end= ' ')
    print()