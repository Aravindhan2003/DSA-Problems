# You are given an array ‘A’ of length ‘N’ consisting only of positive integers and an integer ‘K’.
# You have to update every element of the array by increasing or decreasing its value by ‘K’ only once. 
# Your task is to minimize the difference between maximum and minimum elements of the array 
# after performing the increment or decrement on every element of the array.

# Note: After the operation, every value of the array should remain non-negative.

# For example:

# Let’s say the array ‘A’ = [1, 2, 3, 4, 5] and ‘K’ = 2, then after increasing each element by ‘K’. 
# The array ‘A’ will become [3, 4, 5, 6, 7]. So the maximum - minimum will be 7 - 3 = 4. 

A = [10, 4, 20, 19, 9, 4, 20, 14, 15, 10, 9, 15, 8]
K = 9


def min_difference(A, K):
    min_ele = 99999
    for i in range(len(A)):
        if A[i]-K > 0:
            A[i] = A[i]-K
            if A[i] < min_ele:
                min_ele = A[i]
        else:
            A[i] = A[i]+K

    max_element = A[0]
    min_element = A[0]

    for i in A:
        if i > max_element:
            max_element = i
        
        if i < min_element:
            min_element = i

    return max_element-min_element, min_ele


print(min_difference(A,K))
# print(min_ele)