n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

del blocks[s1-1:e1]
del blocks[s2-1:e2]
print(len(blocks))
for i in range(len(blocks)) :
    print(blocks[i])
