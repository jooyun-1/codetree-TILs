N, M = map(int, input().split())
nums = []

def combination(curr_num, cnt) :
    if curr_num == N+1 :
        if cnt == M :
            for num in nums :
                print(num, end = ' ')
            print()
        return
    
    nums.append(curr_num)
    combination(curr_num+1, cnt+1)
    nums.pop()

    combination(curr_num+1, cnt)

combination(1,0)

