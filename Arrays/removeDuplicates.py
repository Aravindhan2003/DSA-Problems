arr = [0,0,1,1,1,2,2,3,3,4]

for i in range(len(arr)-1):
    print(arr[i])
    print(arr)
    if arr[i] in arr[i+1:]:
        arr.remove(arr[i])
        arr.append('_')
        print(arr)

print(arr)
