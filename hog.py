import random
import unittest
import unittests

############
# Hog Game #
############


# Returns a function that acts as rolling a dice of the specified sides
def dice(sides):
    func = lambda: random.randrange(1, sides+1, step=1)
    func.__name__ = f"d{sides}"
    return func

d4 = dice(4)
d6 = dice(6)
d8 = dice(8)

# Simulate results of rolling num of a specified dice function. Considers sow sad.
def rolls(num_dice, dice):
    results = [dice() for i in range(num_dice)]
    if 1 in results:
        return 1
    else:
        return sum(results)

# Return squared lowest digit of opp_score + 3.
def piggy_points(opp_score):
    def helper(val, arr):
        if val < 10:
            return [val] + arr
        else:
            return helper(val // 10, [val % 10] + arr)
    
    return min(helper(opp_score ** 2, [])) + 3

# Scoring for the current round based on the rules, sow sad, and piggy points.
def scoring(num_dice, opp_score, dice):
    if num_dice == 0:
        return piggy_points(opp_score)
    else:
        return rolls(num_dice, dice)

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

# Return 0 for player 0 or 1 for player 1
def next_player(who):
    return 1 - who

def silence(*args):
    return

def play(strat0, strat1, score0=0, score1=0, start_dice=d6, trot_dice=d8, goal=100, say=silence):
    random.seed()

    def turn(num_dice, player_score, opp_score):
        score = scoring(num_dice, opp_score, dice)
        return player_score + score

    # Presets
    who = 0
    turn_num = 0
    trot = False
    dice = start_dice

    while score0 < goal and score1 < goal:
        if who == 0:
            num_dice = strat0(score0, score1, dice)
            score0 = turn(num_dice, score0, score1)
            trot = time_trot(num_dice, turn_num, trot)
            if not more_boar(score0, score1) and not trot:
                who = next_player(who)
                dice = start_dice
        else:
            num_dice = strat1(score1, score0, dice)
            score1 = turn(num_dice, score1, score0)
            trot = time_trot(num_dice, turn_num, trot)
            if not more_boar(score1, score0) and not trot:
                who = next_player(who)
                dice = start_dice
        turn_num += 1
        dice = trot_dice if trot else dice
        say(score0, score1, num_dice, turn_num, who)
    
    return score0, score1


##############
# Commentary #
##############

def announce_scores(score0, score1, num_dice):
    print(f"After rolling {num_dice}, Player0 has {score0} points. Player1 has {score1} points.")

def announce_turn(turn_num):
    print(f"Turn number: {turn_num}.")

def announce_next_player(who):
    print(f"Next player is {who}.")

def announce_all(score0, score1, num_dice, turn_num, who):
    announce_scores(score0, score1, num_dice)
    print("------")
    announce_next_player(who)
    announce_turn(turn_num)
    

##############
# Strategies #
##############

def winner(score0, score1, goal):
    if score0 >= goal:
        return 0
    elif score1 >= goal:
        return 1
    else:
        None

def strat_rand(player_score, opp_score, dice):
    return random.randrange(0, 10+1, step=1)

def strat_always(n):
    def strat(player_score, opp_score, dice):
        return n
    return strat

def strat_greedy_sim(trials):
        
    def sim(opp_score, dice):
        sim_dict = {key:0 for key in range(11)}
        for num_dice in sim_dict.keys():
            total = 0
            total += scoring(num_dice, opp_score, dice)
            sim_dict[num_dice] = total
        return max(sim_dict, key = sim_dict.get)
    
    def best_num(player_score, opp_score, dice):
        sim_dict = {key:0 for key in range(11)}
        for i in range(trials):
            num = sim(opp_score, dice)
            sim_dict[num] += 1
        return max(sim_dict, key = sim_dict.get)

    return best_num



#tests = unittest.TestLoader().loadTestsFromModule(unittests)
#unittest.TextTestRunner(verbosity=2).run(tests)