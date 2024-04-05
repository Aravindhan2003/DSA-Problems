# You have been given two arrays/list ‘ARR1’ and ‘ARR2’ consisting of ‘N’ and ‘M’ integers respectively. 
# Your task is to return the number of elements common to ‘ARR1’ and ‘ARR2’ and the number of elements 
# in the union of ‘ARR1’ and ‘ARR2’.

# Example:
# Let’s assume ‘ARR1’ is [1,2,3,4,5] and ‘ARR2’ is [2,4,6,8]. 
# Elements common to ‘ARR1’ and ‘ARR2’ are [2,4] as they occur in both ‘ARR1’ and ‘ARR2’. 
# Therefore the number of elements common to ‘ARR1’ and ‘ARR2’ is 2. 
# Union of ‘ARR1’ and ‘ARR2’ is [1,2,3,4,5,6,8]. 
# Therefore the number of distinct elements in the union of ‘ARR1’ and ‘ARR2’ is 7. 
# So, the answer will be 2 7.

def union_intersect(arr1, arr2):

    # initialize the intersection count to 0
    int_count = 0

    # initialize the union count to length of the arr2
    union_count = len(arr2)

    # traverse the arr1
    for i in arr1:

        # check if the element is present in arr2
        if i in arr2:

            # increment the intersection count
            int_count += 1
        else:

            # increment the union count
            union_count += 1

    return int_count, union_count

arr1 =  [1,2,3,4,5]
arr2 = [2,4,6,8]
union_intersect(arr1, arr2)