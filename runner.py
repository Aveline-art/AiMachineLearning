from play import *
import hog
import json

q = dict()

with open("q.txt", "r") as file:
    dicti = json.loads(file.read())
    for key, value in dicti.items():
        new_key = key.split(',')
        a = int(new_key[0][2:])
        b = int(new_key[1][1:])
        c = int(new_key[2][1:])
        d = False if new_key[3][1:] == 'False' else True
        e = new_key[4][2:-2]
        f = int(new_key[5][1:-1])
        q[((a, b, c, d, e), f)] = value

ai = train(100000, q)

def ai_strat(score0, score1, turn_num, trot, dice):
    return ai.make_best_move((score0, score1, turn_num, trot, dice))

score = {
    0: 0,
    1: 0,
}

for i in range(100):
    #print(f"playing game #{i}")
    winner = hog.play(hog.strat_rand, ai_strat)
    score[winner] = score[winner] + 1

with open("q.txt", "w") as file:
    new_dict = dict()
    for key, value in ai.q.items():
        new_dict[str(key)] = value
    file.write(json.dumps(new_dict))
    
print(score)