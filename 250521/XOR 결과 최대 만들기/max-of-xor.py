n, m = map(int, input().split())
A = list(map(int, input().split()))
visited = [
    False for _ in range(n)
]

ans = 0


def calc():
    val = 0
    for i in range(n):
        if visited[i]:
            val ^= A[i]
    
    return val


def find_max_xor(curr_idx, cnt):
    global ans
    
    if cnt == m:
        # 선택된 모든 조합에 대해 xor 연산을 적용해봅니다.
        ans = max(ans, calc())
        return
    
    if curr_idx == n:
        return
    
    # curr_idx index에 있는 숫자를 선택한 경우
    visited[curr_idx] = True
    find_max_xor(curr_idx + 1, cnt + 1)
    visited[curr_idx] = False

    # curr_idx index에 있는 숫자를 선택하지 않은 경우
    find_max_xor(curr_idx + 1, cnt)

find_max_xor(0, 0)

print(ans)