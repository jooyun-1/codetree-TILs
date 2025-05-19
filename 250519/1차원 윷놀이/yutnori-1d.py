n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
pieces = [1] * k
answer = 0

def calc() :
    score = 0
    for piece in pieces :
        if piece >= m :
            score += 1
    return score

def move(cnt) :
    global answer
    answer = max(answer,calc())

    if cnt == n :
        return
    for i in range(k) :
        pieces[i] += nums[cnt]
        move(cnt+1)
        pieces[i] -= nums[cnt]

move(0)
print(answer)