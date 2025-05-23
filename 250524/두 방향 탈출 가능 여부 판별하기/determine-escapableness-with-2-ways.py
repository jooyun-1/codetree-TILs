n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [1,0], [0,1]
answer = 0

def dfs(x,y) :
    global answer
    visited[x][y] = True
    for i in range(2) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == n and ny == m -1 :
            answer = 1
            return
        if nx == n-1 and ny == m :
            answer = 1
            return
        if 0 <= nx < n and 0 <= ny < m :
            if not visited[nx][ny] and grid[nx][ny] == 1:
                dfs(nx,ny)
    
dfs(0,0)
print(answer)

