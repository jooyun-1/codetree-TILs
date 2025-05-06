n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)-1) :
    min_index = i
    temp_index = i
    for j in range(i+1,len(arr)) :
        if arr[min_index] > arr[j] :
            min_val = arr[j]
            min_index = j
    temp = arr[i]
    arr[i] = min_val
    arr[min_index] = temp

for num in arr :
    print(num, end=' ')