# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def remove_duplicates(nums):

    # Initialize left pointer to 0
    left = 0

    # iterate through the list
    for right in range(1, len(nums)):

        # checks both are not equal
        if nums[left] != nums[right]:

            # increment left
            left += 1

            # assign right value to left
            nums[left] = nums[right]

    return left+1

nums = [0,0,1,1,1,2,2,3,3]
remove_duplicates(nums)
