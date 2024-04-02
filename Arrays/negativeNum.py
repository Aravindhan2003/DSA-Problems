# You are given an array 'ARR' consisting of 'N' integers. 
# You need to rearrange the array elements such that all negative numbers appear before all positive numbers.

# Note:
# The order of elements in the resulting array is not important.

# Example:
# Let the array be [1, 2, -3, 4, -4, -5]. 
# On rearranging the array such that all negative numbers appear before 
# all positive numbers we get the resulting array [-3, -5, -4, 2, 4, 1].

def arrange_negative_numbers(arr):
    # left pointer
    start = 0

    # right pointer
    end = len(arr) - 1

    while start < end:
        if arr[start] > 0:
            
            # swap elements
            arr[start], arr[end] = arr[end], arr[start]

            # decrement the right pointer
            end -= 1

        else:
            # increment the left pointer
            start += 1

    return arr


arr = [1, -4, -2, 5, 3]
arrange_negative_numbers(arr)