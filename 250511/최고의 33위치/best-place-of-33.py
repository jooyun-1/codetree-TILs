n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n-2) :
    cnt = 0
    for a in range(i,i+3) :
        for b in range(i,i+3) :
            if grid[a][b] == 1 :
                cnt += 1
    answer = max(answer,cnt)
print(answer)