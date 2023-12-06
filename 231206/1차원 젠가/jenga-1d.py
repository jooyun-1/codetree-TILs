n = int(input())
arr = []
for i in range(n) :
    num = int(input())
    arr.append(num)
remove_info = []
for i in range(2) :
    first, last = map(int,input().split())
    remove_info.append([first-1,last-1])
for i in range(2) :
    first,last = remove_info.pop(0)
    arr = arr[:first] + arr[last+1:]
print(len(arr))
for i in range(len(arr)) :
    print(arr[i])