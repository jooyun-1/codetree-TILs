n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
answer = 0

for edge in edges :
    a, b = edge[0], edge[1]
    graph[a].append(b)
    graph[b].append(a)

def dfs(node) :
    global answer
    visited[node] = True
    for n in graph[node] :
        if not visited[n] :
            answer += 1
            dfs(n) 

dfs(1)
print(answer)