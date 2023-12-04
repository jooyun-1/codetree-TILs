def move(row,dir) :
    if row >=0 and row < len(board) and visited[row] == 0 :
        visited[row] = 1
        if dir == 'L' :
            temp = board[row][-1]
            for i in range(M-1,-1,-1) :
                board[row][i] = board[row][i-1]
            board[row][0] = temp

            check(row,dir)
        elif dir == 'R' :
            temp = board[row][0]
            for i in range(1,M) :
                board[row][i-1] = board[row][i]
            board[row][-1] = temp

            check(row,dir)
            

def check(row,dir) :
    for i in range(len(board[row])) :
        if row - 1 >= 0 and board[row][i] == board[row-1][i] :
            if dir == 'L' :
                move(row-1,'R')
            elif dir == 'R' :
                move(row-1,'L')
        elif row + 1 < len(board) and board[row][i] == board[row+1][i] :
            if dir == 'L' :
                move(row+1,'R')
            elif dir == 'R' :
                move(row+1,'L')

N, M, Q = map(int,input().split())
board = []
# board 입력
for n in range(N) :
    line = list(map(int,input().split()))
    board.append(line)
winds = []
# 바람 입력
for q in range(Q) :
    r, d = input().split()
    winds.append([int(r)-1,d])
for w in winds :
    visited = [0] * N
    move(w[0],w[1])
for i in range(len(board)) :
    for j in range(len(board[i])) :
        print(board[i][j], end=' ')
    print()