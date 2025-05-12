n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# 3 1
# 1 2 3
# 1 5 6
# [1, 1, 2] [5, 6, 3]
time = 0
d.reverse()
while time < t :
    
    u_start, u_end = u[0], u[-1]
    d_start, d_end = d[0], d[-1]

    for i in range(n-1,0,-1) :
        u[i] = u[i-1]
    for i in range(n-1) :   
        d[i] = d[i+1]
    u[0] = d_start
    d[-1] = u_end
    time += 1
d.reverse()
for num in u :
    print(num, end= ' ')
print()
for num in d :
    print(num, end = ' ')

