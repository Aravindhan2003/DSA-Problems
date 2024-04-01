# You are given an array ‘Arr’ consisting of ‘N’ distinct integers and a positive integer ‘K’. 
# Find out Kth smallest and Kth largest element of the array. 
# It is guaranteed that K is not greater than the size of the array.

def kMaxMin(arr, k):
    '''
        Returns the Kth smallest and largest number in the array.
    '''

    # sort the array(selection sort)
    start = 0
    for _ in range(len(arr)):
        min_ele = arr[start]
        min_index = start
        for i in range(start+1, len(arr)):
            if arr[i] < min_ele:
                min_index = i
                min_ele = arr[i]
                arr[start], arr[min_index] = arr[min_index], arr[start]

        start += 1

    # find the kth smallest from the sorted array
    k_small = arr[k-1]

    # find the kth largest from the sorted array
    k_large = arr[-k]

    return k_small, k_large


arr = [5, 4, 3, 2, 1]
k = 3
print(kMaxMin(arr, k))
