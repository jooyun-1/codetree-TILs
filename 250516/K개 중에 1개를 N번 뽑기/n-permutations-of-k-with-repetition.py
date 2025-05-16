K, N = map(int, input().split())
selected_nums = []

def select(cnt) :
    if cnt == N :
        for num in selected_nums :
            print(num, end=' ')
        print()
        return
    for i in range(1,K+1) :
        selected_nums.append(i)
        select(cnt+1)
        selected_nums.pop()
select(0)
