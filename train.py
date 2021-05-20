from hog import *
from hog_ai import *
import random

def train(ai, num_games, say=lambda x: None):

    def ai_strat(player_score, opp_score, dice):
        return ai.make_move((player_score, opp_score))


    for i in range(num_games):
        say(i)

        data = {
            0: {"prev_state": None, "action": None, "new_state": None},
            1: {"prev_state": None, "action": None, "new_state": None},
        }

        
        def save_data(player, prev_state, action, new_state):
            data[player]["prev_state"] = prev_state
            data[player]["action"] = action
            data[player]["new_state"] = new_state
    
        # defaults
        strat0 = ai_strat
        strat1 = ai_strat
        score0 = 0
        score1 = 0
        start_dice = d6
        trot_dice = d8
        goal = 100

        def turn(num_dice, player_score, opp_score):
            score = scoring(num_dice, opp_score, dice)
            return player_score + score
        
        # presets
        who = 0
        turn_num = 0
        trot = False
        dice = start_dice

        def save_state(player):
            if player == 0:
                state = (score0, score1)
            elif player == 1:
                state = (score1, score0)
            return state

        while score0 < goal and score1 < goal:
            start_state = save_state(who)
            if who == 0:
                num_dice = strat0(score0, score1, dice)
                score0 = turn(num_dice, score0, score1)
                trot = time_trot(num_dice, turn_num, trot)
                turn_num += 1
                dice = trot_dice if trot else dice
                end_state = save_state(who)
                save_data(who, start_state, num_dice, end_state)
                if not more_boar(score0, score1) and not trot:
                    who = next_player(who)
                    dice = start_dice
            else:
                num_dice = strat1(score1, score0, dice)
                score1 = turn(num_dice, score1, score0)
                trot = time_trot(num_dice, turn_num, trot)
                turn_num += 1
                dice = trot_dice if trot else dice
                end_state = save_state(who)
                save_data(who, start_state, num_dice, end_state)
                if not more_boar(score1, score0) and not trot:
                    who = next_player(who)
                    dice = start_dice
            
            win_player = winner(score0, score1, goal)
            if win_player != None:
                ai.update(
                    start_state,
                    end_state,
                    num_dice,
                    1
                )
                ai.update(
                    data[1-win_player]["prev_state"],
                    data[1-win_player]["new_state"],
                    data[1-win_player]["action"],
                    -1
                )
            else:
                ai.update(start_state, end_state, num_dice, 0)
            
    return ai

def test(num_games, ai, strat):
    def ai_strat(player_score, opp_score, dice):
        return ai.make_best_move((player_score, opp_score))
    
    score = 0

    for i in range(num_games):
        ai_first = random.choice([True, False])
        if ai_first:
            score0, score1 = play(ai_strat, strat)
            player = winner(score0, score1, 100)
            score += 1 if player == 0 else 0
        else:
            score0, score1 = play(strat, ai_strat)
            player = winner(score0, score1, 100)
            score += 1 if player == 1 else 0
    
    return score / num_games
    



