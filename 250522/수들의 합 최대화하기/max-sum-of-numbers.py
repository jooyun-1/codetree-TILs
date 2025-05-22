n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited = [False] * n
picked = []
ans = 0

def select_color(row) :
    global ans 

    if row == n :
        total = 0
        for i in range(n) :
            total += grid[i][picked[i]]
        ans = max(ans,total)
     
    for i in range(n) :
        if visited[i] :
            continue
        visited[i] = True
        picked.append(i)
        select_color(row+1)
        picked.pop()
        visited[i] = False

select_color(0)
print(ans)
