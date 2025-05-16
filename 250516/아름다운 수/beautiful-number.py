n = int(input())
seq = []
answer = 0

def is_beautiful() :
    i = 0
    while i < n :
        if i + seq[i] - 1 >= n :
            return False
        for j in range(i,i+seq[i]) :
            if seq[j] != seq[i] :
                return False
        i += seq[i]
    return True
def select(cnt) :
    global answer
    if cnt == n :
        if is_beautiful() :
            answer += 1
        return
    for i in range(1,5) :
        seq.append(i)
        select(cnt+1)
        seq.pop()

select(0)
print(answer)
