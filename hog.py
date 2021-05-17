import random

# Returns a function that acts as rolling a dice of the specified sides
def dice(sides):
    return lambda: random.randrange(1, sides+1, step=1)

# Simulate rolling num of a specified dice function
def rolls(num, dice):
    return [dice() for val in range(num)]

# Returns a score of 1 if any rolls are 1
def sow_sad(results):
    if 1 in results:
        return 1
    else:
        return None

# If number of dice rolled is 0, return squared lowest digit of opp_score + 3
def piggy_points(opp_score):
    def helper(val, arr):
        if val // 10 == 0:
            return arr + [val]
        else:
            return helper(val // 10, arr + [val % 10])
    
    return min(helper(opp_score, [])) ** 2 + 3

# Returns the new current_score
def scoring(results, current_score, opp_score):
    return