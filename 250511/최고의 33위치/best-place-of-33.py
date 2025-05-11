n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def get_coins(r,r2,c,c2) :
    cnt = 0
    for i in range(r, r2+1) :
        for j in range(c, c2+1) :
            if grid[i][j] == 1 :
                cnt += 1
    return cnt

for i in range(n) :
    for j in range(n) :
        if i + 2 >= n or j + 2 >= n :
            continue
        answer = max(answer,get_coins(i,i+2,j,j+2))    
print(answer)