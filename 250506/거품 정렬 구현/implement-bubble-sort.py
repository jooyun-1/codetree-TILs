n = int(input())
arr = list(map(int, input().split()))
flag = False
while flag == False :
    flag = True
    for i in range(len(arr)-1) :
        if arr[i] > arr[i+1] :
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            flag = False
for num in arr :
    print(num, end= ' ')