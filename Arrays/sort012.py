# You have been given an integer array/list(ARR) of size 'N'. 
# It only contains 0s, 1s and 2s. Write a solution to sort this array/list.

# Note :
# Try to solve the problem in 'Single Scan'. 
# ' Single Scan' refers to iterating over the array/list just once or to put it in other words, 
# you will be visiting each element in the array/list just once.

arr = [0, 1, 2, 1, 2, 1, 2]
new_arr = [0, 0, 0, 0, 0, 0, 0]

zero_index = 0
one_index = 1
two_index = 2

for i in arr:
    if i == 0:
        new_arr.insert(zero_index, i)
        zero_index += 1
        one_index += 1
        two_index += 1
    
    elif i == 1:
        new_arr.insert(one_index, i)
        one_index += 1
        two_index += 1

    elif i == 2:
        new_arr.insert(two_index, i)
        two_index += 1

    print(new_arr)
    
print(new_arr)    