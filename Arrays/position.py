# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

def findPosition(nums, target):
    if target not in nums:
        return [-1, -1]

    else:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start+end)//2
            if nums[mid] < target:
                start = mid+1

            elif nums[mid] > target:
                end = mid-1

            else:
                # start = mid
                if nums[end] > target:
                    end -= 1
                else:
                    return [mid, end]

nums = [1, 1, 1]
target = 1
print(findPosition(nums, target))

# incomplete