import random
import unittest
import unittests

# Returns a function that acts as rolling a dice of the specified sides
def dice(sides):
    func = lambda: random.randrange(1, sides+1, step=1)
    func.__name__ = f"d{sides}"
    return func

d4 = dice(4)
d6 = dice(6)
d8 = dice(8)

# Simulate rolling num of a specified dice function
def rolls(num_dice, dice):
    return [dice() for i in range(num_dice)]

# Returns a score of 1 if any rolls are 1
def sow_sad(results):
    if 1 in results:
        return 1
    else:
        return None

# If number of dice rolled is 0, return squared lowest digit of opp_score + 3
def piggy_points(opp_score):
    def helper(val, arr):
        if val < 10:
            return [val] + arr
        else:
            return helper(val // 10, [val % 10] + arr)
    
    return min(helper(opp_score, [])) ** 2 + 3

# Returns true if the player can take another turn, based on more_boar
def more_boar(player_score, opp_score):
    def helper(val, arr):
        if val < 10:
            if not arr:
                return [0] + [val]
            return [val] + arr
        else:
            return helper(val // 10, [val % 10] + arr)
    
    player_split = helper(player_score, [])
    opp_split = helper(opp_score, [])
    if player_split[0] < opp_split[0] and player_split[1] < opp_split[1]:
        return True
    else:
        return False

# Returns true if conditions for time_trot is met, else false
def time_trot(num_dice, turn_num, trot):
    if num_dice == turn_num % 8 and not trot:
        return True
    else:
        return False

# Returns the end score for player after taking a turn, considering sow_sad and piggy_points
def turn(num_dice, dice, player_score, opp_score):
    # Player new score if piggy points
    if num_dice == 0:
        return player_score + piggy_points(opp_score)
    results = rolls(num_dice, dice)

    # Player new score if sow sad
    is_sow_sad = sow_sad(results)
    if is_sow_sad:
        return player_score + is_sow_sad
    
    # Player score if regular
    return player_score + sum(results)

# Return 0 for player 0 or 1 for player 1 based on more_boar and time_trot
def next_turn_player(current_player, more_boar, time_trot):
    if more_boar:
        return current_player
    if time_trot:
        return current_player
    else:
        return 1 - current_player

def play(strat0, strat1, score0=0, score1=0, start_dice=d6, goal=100):
    random.seed() 

    # Presets  
    current_player = 0
    turn_num = 0
    trot = False
    current_dice = start_dice
    winner = has_won(score0, score1, goal)

    # While loop for the game. Mayber use a recursion somewhere?
    while winner not in [0, 1]:
        if current_player == 0:
            # Pick number of dice based on strategy
            num_dice = strat0(score0, score1, turn_num, trot, current_dice.__name__)

            # Find if dice chosen results in trot
            trot = time_trot(num_dice, turn_num, trot)

            # If a trot ever happens, just once, dice changes
            if trot:
                current_dice = d8
            
            # Calculate new score
            score0 = turn(num_dice, current_dice, score0, score1)

            # Determine next player based on more_boar and trot
            next_player = next_turn_player(current_player, more_boar(score0, score1), trot)
        else:
            # Pick number of dice based on strategy
            num_dice = strat1(score1, score0, turn_num, trot, current_dice.__name__)

            # Find if dice chosen results in trot
            trot = time_trot(num_dice, turn_num, trot)

            # If a trot ever happens, just once, dice changes
            if trot:
                current_dice = d8

            # Calculate new score
            score1 = turn(num_dice, current_dice, score1, score0)

            # Determine next player based on more_boar and trot
            next_player = next_turn_player(current_player, more_boar(score1, score0), trot)
        
        # Turn counter goes up after a player takes a turn
        turn_num += 1

        # Resets dice when player switches
        if current_player != next_player:
            current_dice = start_dice
        
        # Set next player
        current_player = next_player

        #print(f"Player0 score is {score0} and Player1 score is {score1}. Next player is {current_player}. Current dice is {current_dice.__name__}")

        # Determine if anyone has won
        winner = has_won(score0, score1, goal)
    
    #print(f"Winner is: {winner}.")
    return winner

# Returns the winner based on scores. None if no one wins.
def has_won(score0, score1, goal):
    if score0 >= goal:
        return 0
    elif score1 >= goal:
        return 1
    else:
        return None

def strat_rand(score0, score1, turn_num, trot, dice):
    return random.randrange(0, 10+1, step=1)

def strat_six(score0, score1, turn_num, trot, dice):
    return 6

#tests = unittest.TestLoader().loadTestsFromModule(unittests)
#unittest.TextTestRunner(verbosity=2).run(tests)