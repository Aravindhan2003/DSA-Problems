# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

def findTwoSum(nums, target):
    for i in range(len(nums)):
        diff = target-nums[i]
        if diff in nums[i+1:]:
            return i, (nums[i+1:].index(diff)+i+1)


nums = [15,7,11,2]
target = 9
findTwoSum(nums, target)