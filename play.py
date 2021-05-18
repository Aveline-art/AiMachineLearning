from hog import *
from hog_ai import *

def train(num_games, q):
    ai = HogAI()
    ai.q = q

    def ai_strat(score0, score1, turn_num, trot, dice):
        return ai.make_move((score0, score1, turn_num, trot, dice))


    for i in range(num_games):
        #print(f"playing game #{i}")

        data = {
            0: {"old_state": None, "action": None, "new_state": None},
            1: {"old_state": None, "action": None, "new_state": None},
        }
    
        score0 = 0
        score1 = 0
        goal = 100
        current_player = 0
        turn_num = 0
        trot = False
        current_dice = d6
        winner = has_won(score0, score1, goal)

        while winner not in [0, 1]:
            if current_player == 0:
                state = (score0, score1, turn_num, trot, current_dice.__name__)
                num_dice = ai_strat(score0, score1, turn_num, trot, current_dice.__name__)

                trot = time_trot(num_dice, turn_num, trot)
                if trot:
                    current_dice = d8
                score0 = turn(num_dice, current_dice, score0, score1)
                next_player = next_turn_player(current_player, more_boar(score0, score1), trot)
            else:
                state = (score1, score0, turn_num, trot, current_dice.__name__)
                num_dice = ai_strat(score1, score0, turn_num, trot, current_dice.__name__)

                trot = time_trot(num_dice, turn_num, trot)
                if trot:
                    current_dice = d8
                score1 = turn(num_dice, current_dice, score1, score0)
                next_player = next_turn_player(current_player, more_boar(score1, score0), trot)
            turn_num += 1
            if current_player != next_player:
                current_dice = d6
            current_player = next_player
            winner = has_won(score0, score1, goal)

            curr_state = (score0, score1, turn_num, trot, current_dice.__name__)

            if winner:
                old_state = data[winner]["old_state"]
                action = num_dice
                new_state = curr_state
                ai.update(old_state, new_state, action, 1)

                old_state = data[1-winner]["old_state"]
                action = data[1-winner]["action"]
                new_state = data[1-winner]["new_state"]
                ai.update(old_state, new_state, action, -1)
            else:
                data[current_player]["old_state"] = state
                data[current_player]["action"] = num_dice
                data[current_player]["new_state"] = curr_state
                ai.update(state, curr_state, num_dice, 0)
    
    return ai
    



