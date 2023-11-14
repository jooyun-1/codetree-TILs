import sys

N = int(sys.stdin.readline())
board = []
for n in range(N) :
    line = list(map(int,sys.stdin.readline().split()))
    board.append(line)
money = 0
for i in range(len(board)) :
    for j in range(len(board[i])) :
        cnt = 0
        for a in range(3) :
            for b in range(3) :
                if i + a >= len(board) or j + b >= len(board[i]) :
                    break
                else :
                    if board[i+a][j+b] == 1 :
                        cnt += 1
        money = max(cnt,money)
print(money)