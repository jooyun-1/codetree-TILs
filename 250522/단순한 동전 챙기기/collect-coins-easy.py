import sys

n = int(input())
m = 3
grid = [list(input()) for _ in range(n)]
coins = [i for i in range(1,10)]
coin_pos = list()
selected_pos = list()
ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_pos = (i, j)
        if grid[i][j] == 'E':
            end_pos = (i, j)

for num in range(1,10) :
    for i in range(n) :
        for j in range(n) :
            if grid[i][j] == str(num) :
                coin_pos.append((i,j))
def dist(a,b) :
    (ax,ay), (bx,by) = a, b
    return abs(ax - bx) + abs(ay - by)

def calc() :
    moves = dist(start_pos, selected_pos[0])
    for i in range(m-1) :
        moves += dist(selected_pos[i], selected_pos[i+1])
    moves += dist(selected_pos[m-1],end_pos)
    return moves

def select_coin(cur_index, cnt) :
    global ans
    if cnt == m :
        ans = min(ans,calc())
    if cur_index == len(coin_pos) :
        return
    selected_pos.append(coin_pos[cur_index])
    select_coin(cur_index+1, cnt+1)
    selected_pos.pop()

    select_coin(cur_index+1, cnt)

select_coin(0,0)
if ans == sys.maxsize:
    ans = -1
print(ans)