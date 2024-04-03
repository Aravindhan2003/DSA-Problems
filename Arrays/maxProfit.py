# You are given an array/list 'prices' where the elements of the array represent the prices of the stock 
# as they were yesterday and indices of the array represent minutes. 
# Your task is to find and return the maximum profit you can make by buying and selling the stock. 
# You can buy and sell the stock only once.

# Note:

# You can’t sell without buying first.
# For Example:
# For the given array [ 2, 100, 150, 120],
# The maximum profit can be achieved by buying the stock at minute 0 when its price is Rs. 2 
# and selling it at minute 2 when its price is Rs. 150.
# So, the output will be 148.

arr = [2, 100, 150, 120, 180]

left = 0
right = 1
max_profit = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] - arr[i] > max_profit:
            max_profit = arr[j] - arr[i]

print(max_profit)

# while left < right:
#     if arr[right] - arr[left] > max_profit:
#         max_profit = arr[right] - arr[left]
    
#     # else:
#     #     left += 1
#     print(max_profit)
#     right += 1

# for i in arr:
#     if arr[right] - i > max_profit:
#         max_profit = arr[right] - i

#     right += 1
    
