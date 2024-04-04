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

def maximumProfit(arr):
    min_price = arr[0]
    max_profit = 0

    for i in range(1, len(arr)):
        if arr[i] < min_price:
            min_price = arr[i]
        
        else:
            profit = arr[i] - min_price
            if max_profit < profit:
                max_profit = profit

    return max_profit

arr = [2, 100, 1, 150, 120, 200]
maximumProfit(arr)

    
