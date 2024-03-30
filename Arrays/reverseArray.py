# Given an array/list 'ARR' of integers and a position ‘M’. You have to reverse the array after that position.

# Example:

# We have an array ARR = {1, 2, 3, 4, 5, 6} and M = 3 , considering 0 
# based indexing so the subarray {5, 6} will be reversed and our 
# output array will be {1, 2, 3, 4, 6, 5}.

def reverse_subarray(arr, m):
    # left pointer
    left = m + 1

    # right pointer
    right = len(arr) - 1

    while (left < right):
        # swap elements
        arr[left], arr[right] = arr[right], arr[left]

        # increment left and right after each swap
        left += 1
        right -= 1

    return arr


arr = [1, 4, 5, 6, 6, 7, 7]
m = 3
reverse_subarray(arr, m)