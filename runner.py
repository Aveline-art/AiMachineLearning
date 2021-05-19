from train import *
import hog
import json
import pprint as pp

q = dict()

with open("q2.txt", "r") as file:
    dicti = json.loads(file.read())
    for key, value in dicti.items():
        if key == '(None, None)':
            continue
        new_key = key.split(',')
        a = int(new_key[0][2:])
        b = int(new_key[1][1:-1])
        d = int(new_key[2][1:-1])
        q[((a, b), d)] = value

def speak(x):
    if x % 10000 == 0:
        print(f"Now on game {x/10000}")

ai = train(0, q, speak)

def ai_strat(player_score, opp_score, dice):
    return ai.make_best_move((player_score, opp_score))

score = {
    0: 0,
    1: 0,
}

for i in range(1000):
    #print(f"playing game #{i}")
    score0, score1 = hog.play(ai_strat, hog.strat_rand)
    player = winner(score0, score1, 100)
    score[player] = score[player] + 1

print(score)
'''
with open("q2.txt", "w") as file:
    new_dict = dict()
    for key, value in ai.q.items():
        new_dict[str(key)] = value
    file.write(json.dumps(new_dict))'''