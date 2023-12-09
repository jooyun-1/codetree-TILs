n, r, c = map(int,input().split())
board = []
for i in range(n) :
    line = list(map(int,input().split()))
    board.append(line)
r -= 1
c -= 1
answer = []
answer.append(board[r][c])
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def search(x,y) :
    flag = False
    cur_val = board[x][y]
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if cur_val < board[nx][ny] :
                answer.append(board[nx][ny])
                flag = True
                search(nx,ny)
            if flag :
                break
    if flag == False :
        return
search(r,c)
for i in range(len(answer)) :
    print(answer[i], end = ' ')