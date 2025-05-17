import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# [i] == 1 -> 
dx1, dy1 = [1,-1,2,-2], [0,0,0,0]
# [i] == 2 ->
dx2, dy2 = [1,-1,0,0], [0,0,1,-1]
# [i] == 3 -> 
dx3, dy3 = [1,-1,1,-1], [1,-1,-1,1]

bombs = []
arr = []
answer = 0

for i in range(len(grid)) :
    for j in range(len(grid[i])) :
        if grid[i][j] == 1 :
            arr.append((i,j))
bombs_length = len(arr)

def count_blocks() :
    temp = [row[:] for row in grid]
    que = arr[:]
    
    block = 0
    index = 0
    while que :
        x, y = que.pop(0)
        bomb = bombs[index]
        for i in range(4) :
            if bomb == 1 :
                nx, ny = x + dx1[i], y + dy1[i]
                if 0 <= nx < n and 0 <= ny < n :
                    if temp[nx][ny] == 0 :
                        temp[nx][ny] = 1
            elif bomb == 2 :
                nx, ny = x + dx2[i], y + dy2[i]
                if 0 <= nx < n and 0 <= ny < n :
                    if temp[nx][ny] == 0 :
                        temp[nx][ny] = 1
            elif bomb == 3 :
                nx, ny = x + dx3[i], y + dy3[i]
                if 0 <= nx < n and 0 <= ny < n :
                    if temp[nx][ny] == 0 :
                        temp[nx][ny] = 1
        index += 1
    for i in range(len(temp)) :
        for j in range(len(temp[i])) :
            if temp[i][j] == 1 :
                block += 1
    return block

def select_bombs(cnt) :
    global answer
    if cnt == bombs_length :
        answer = max(answer,count_blocks())
        return
    for i in range(1,4) :
        bombs.append(i)
        select_bombs(cnt+1)
        bombs.pop()

select_bombs(0)
print(answer)
