# You are given an array “ARR” of size N. 
# Your task is to find out the sum of maximum and minimum elements in the array.

def findMinMaxSum(arr):
    '''
        Returns the sum of minimum and maximum element of the list
    '''
    
    # find minimum element
    min_ele = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_ele:
            min_ele = arr[i]

    # find maximum element
    max_ele = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_ele:
            max_ele = arr[i]

    return (min_ele + max_ele)

arr = [-1, -4, 5, 8, 9, 3]
findMinMaxSum(arr)