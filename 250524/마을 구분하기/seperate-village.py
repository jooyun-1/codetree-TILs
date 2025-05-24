n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnts = []
village_cnt = 0
dx, dy = [1,-1,0,0], [0,0,1,-1]

def dfs(x,y) :
    global people
    people += 1
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if grid[nx][ny] == 1 and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                dfs(nx,ny)

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 1 and visited[i][j] == 0 :
            visited[i][j] = 1
            people = 0
            village_cnt += 1
            dfs(i,j)
            cnts.append(people)
cnts.sort()
print(village_cnt)
for cnt in cnts :
    print(cnt)