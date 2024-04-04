# You have been given an integer array/list(ARR) of size 'N'. 
# It only contains 0s, 1s and 2s. Write a solution to sort this array/list.

# Note :
# Try to solve the problem in 'Single Scan'. 
# ' Single Scan' refers to iterating over the array/list just once or to put it in other words, 
# you will be visiting each element in the array/list just once.

def sorting012(arr):

    # initialize the position of zero as 0
    zero = 0

    # initialize the current position
    current = 0

    # initialize the position of 2 as len(arr)-1 [last index]
    two = len(arr)-1

    while current <= two:
        if arr[current] == 0:

            # swap the elements
            arr[zero], arr[current] = arr[current], arr[zero]

            # increment the zero position
            zero += 1

            # increment the current position
            current += 1

        elif arr[current] == 1:

            # increment the current position
            current += 1

        elif arr[current] == 2:

            # swap the elements
            arr[two], arr[current] = arr[current], arr[two]

            # decrement the two position
            two -= 1
        
    return arr

arr = [0, 1, 1, 0, 0, 1, 1, 0, 1, 0]
sorting012(arr)
