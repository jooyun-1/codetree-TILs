N, M = map(int,input().split())
board = []
for n in range(N) :
    line = list(map(int,input().split()))
    board.append(line)
answer = 0
for i in range(N) :
    temp = []
    for j in range(N-1) :
        if board[i][j] == board[i][j+1] :
            temp.append(board[i][j])
            temp.append(board[i][j+1])
            if len(temp) == M :
                answer += 1
                break
for i in range(N) :
    temp = []
    for j in range(N-1) :
        if board[j][i] == board[j+1][i] :
            temp.append(board[i][j])
            temp.append(board[i][j+1])
            if len(temp) == M :
                answer += 1
                break
arr = []
if M == 1 :
    for i in range(N) :
        for j in range(N) :
            arr.append(board[i][j])
    arr = list(set(arr))
    answer = len(arr)
print(answer)