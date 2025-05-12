n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = -1

shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

def max_sum(x,y) :
    max_val = 0
    for i in range(6) :
        result = 0
        is_possible = True
        for dx in range(3) :
            for dy in range(3) :
                if shapes[i][dx][dy] == 0 :
                    continue
                if x + dx >= n or y + dy >= m:
                    is_possible = False
                else:
                    result += grid[x + dx][y + dy]
        if is_possible:
            max_val = max(max_val, result)  
    return max_val            

for i in range(n) :
    for j in range(m) :
        answer = max(answer,max_sum(i,j))
print(answer)