N, M = map(int,input().split())
board = []
for n in range(N) :
    line = list(map(int,input().split()))
    board.append(line)
answer = 0
if M == 1 :
    answer = 2*N
else :
    for i in range(N) :
        temp = []
        for j in range(N-1) :
            if board[i][j] == board[i][j+1] :
                # print(i,j,board[i][j],board[i][j+1])
                temp.append(board[i][j])
                # temp.append(board[i][j+1])
                if len(temp) == M :
                    # print(temp)
                    answer += 1
                    # print(answer)
                    break
    for i in range(N) :
        temp = []
        for j in range(N-1) :
            if board[j][i] == board[j+1][i] :
                temp.append(board[i][j])
                # temp.append(board[i][j+1])
                if len(temp) == M :
                    answer += 1
                    break
print(answer)