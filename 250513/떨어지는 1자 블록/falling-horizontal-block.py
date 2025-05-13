n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
block = [1] * m

# n*n, 1*m크기, 시작 열 : k-1, k+m-2
row = 0
def check_grid(row) :
    for j in range(k-1,k+m-1) :
        if grid[row+1][j] == 1 :
            return True
    return False

while True :
    if row + 1 >= n :
        for i in range(k-1,k+m-1) :
            grid[row][i] = 1
        break        
    else :
        flag = check_grid(row)
        if flag :
            for i in range(k-1,k+m-1) :    
                grid[row][i] = 1
            break
    row += 1

for i in range(len(grid)) :
    for j in range(len(grid[i])) :
        print(grid[i][j], end = ' ')
    print()