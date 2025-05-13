from collections import deque

n, r, c = map(int, input().split()) # r, c : 시작 행,열
a = [[0] * n for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        a[i][j] = row[j]

dx, dy = [-1,1,0,0], [0,0,-1,1]
que = deque()
arr = [a[r-1][c-1]]

def bfs(i,j) :
    que.append((i,j))
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if a[nx][ny] > a[x][y] :
                    que.append((nx,ny))
                    arr.append(a[nx][ny])
                    break
bfs(r-1,c-1)
for num in arr :
    print(num, end=' ')
