# You are keeping the scores for a baseball game with strange rules. 
# At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is 
# the ith operation you must apply to the record and is one of the following:

# 0. An integer x.
# Record a new score of x.
# 1. '+'.
# Record a new score that is the sum of the previous two scores.
# 2. 'D'.
# Record a new score that is the double of the previous score.
# 3. 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

def calulatePoints(operations:list[str]):
    record = []
    for i in operations:
        if i == 'C':
            record.pop()
        
        elif i == 'D':
            record.append(2*record[-1])
        
        elif i == '+':
            record.append(record[-1] + record[-2])

        else:
            record.append(int(i))

    total_sum = 0
    for j in record:
        total_sum += j

    return total_sum

ops = ["5","-2","4","C","D","9","+","+"]
print(calulatePoints(ops))