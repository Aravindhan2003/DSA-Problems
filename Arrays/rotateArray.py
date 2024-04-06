arr = [1,2,3,4,5]
k = 3





while k > 0:
    current = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]

    arr[-1] = current
    k -= 1

print(arr)

