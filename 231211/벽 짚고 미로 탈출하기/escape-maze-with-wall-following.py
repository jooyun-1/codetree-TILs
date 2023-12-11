# 1. 바라보고 있는 방향 이동 불가
# 반시계 방향으로 90도 방향 바꿈 : dir = [[~],[~]]
# 2. 바라보고 있는 방향 이동 가능
# 바로 앞이 격자 밖이면 이동하여 탈출
# 아닐 때, 현재 방향으로 한칸 이동했을 때, '지금 바라보는 방향'의 오른쪽에 벽이 있으면 앞으로 한 칸 이동
# 현재 방향으로 한칸 이동했을 때, 벽 없으면 시계방향으로 90도 방향 틀어 한칸 더 전진
def escape(x,y,cur_dir) :
    global time

    if visited[x][y] == 0 :
        visited[x][y] = 1
    else :
        time = -1
        return
    dirs = [[0,1],[-1,0],[0,-1],[1,0]]
    clock_dirs = [[0,1],[1,0],[0,-1],[1,0]]
    nx = x + dirs[cur_dir][0]
    ny = y + dirs[cur_dir][1]

    visited.append([x,y])

    if 0 <= nx < N and 0 <= ny < N :
        if miro[nx][ny] == '#' :
            cur_dir = (cur_dir+1) % 4
            escape(x,y,cur_dir)
        else :
            right_dir = cur_dir - 1
            if right_dir < 0 :
                right_dir = 3
            # right_dir = (cur_dir+1) % 4
            # rx = nx + clock_dirs[right_dir][0]
            # ry = ny + clock_dirs[right_dir][1]
            rx = nx + dirs[right_dir][0]
            ry = ny + dirs[right_dir][1]
            if 0 <= rx < N and 0 <= ry < N :
                if miro[rx][ry] == '#' :
                    time += 1
                    escape(nx,ny,cur_dir)
                else :
                    time += 2
                    escape(rx,ry,right_dir)
    else :
        time += 1

N = int(input())
x, y = map(int,input().split())
x -= 1
y -= 1
miro = []
visited = [[0] * N for _ in range(N)]
for n in range(N) :
    line = input().rstrip()
    temp = []

    for i in range(len(line)) :
        temp.append(line[i])
    miro.append(temp)
time = 0
escape(x,y,0)
print(time)