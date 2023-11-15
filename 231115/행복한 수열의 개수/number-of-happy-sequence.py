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
        cnt = 0
        for j in range(N-1) :
            if board[i][j] == board[i][j+1] :
                cnt += 1
                if cnt == M-1 :
                    answer += 1
                    break
            else :
                cnt = 0
    for i in range(N) :
        cnt = 0
        for j in range(N-1) :
            if board[j][i] == board[j+1][i] :
                cnt += 1
                if cnt == M-1 :
                    answer += 1
                    break
            else :
                cnt = 0
print(answer)