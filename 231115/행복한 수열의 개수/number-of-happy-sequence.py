N, M = map(int,input().split())
board = []
for n in range(N) :
    line = list(map(int,input().split()))
    board.append(line)
answer = 0
for i in range(N) :
    temp = 0
    for j in range(N-1) :
        if board[i][j] == board[i][j+1] :
            temp += 1
            if temp == M-1 :
                answer += 1
                break
for i in range(N) :
    temp = 0
    for j in range(N-1) :
        if board[j][i] == board[j+1][i] :
            temp += 1
            if temp == M-1 :
                answer += 1
                break
print(answer)