n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [1,0], [0,1]

def dfs(x,y) :
    for i in range(2) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = 1
                dfs(nx,ny)
visited[0][0] = 1
dfs(0,0)
print(visited[n - 1][m - 1])

