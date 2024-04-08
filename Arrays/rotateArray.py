def reverse_list(arr, start, end, left=0, right=0):
    while start < end or left < right:
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

def rotate_array(arr, k):

    # reverse the entire list 
    reverse_list(arr, 0, len(arr)-1)

    # reverse the sub-arrays separately
    reverse_list(arr, 0, len(arr)-k-1, len(arr), len(arr)-1)
    
    return arr

arr = [1,2,3,4,5]
k = 3

rotate_array(arr, k)


