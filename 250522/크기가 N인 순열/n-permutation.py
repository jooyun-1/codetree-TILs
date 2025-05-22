n = int(input())
visited = [False] * (n+1)
answer = []

def permutation(curr_num) :
    if curr_num == n + 1 :
        for ans in answer :
            print(ans, end = ' ')
        print()
        return
    
    for i in range(1,n+1) :
        if visited[i] :
            continue
        visited[i] = True
        answer.append(i)
        permutation(curr_num + 1)
        answer.pop()
        visited[i] = False

permutation(1)
