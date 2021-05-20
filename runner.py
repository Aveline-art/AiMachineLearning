from experiment import *

num_trainings = 10
num_batches = 10
num_test_games = 1000

ai = HogAI(q=dict())
print(len(ai.q))

#x, y = trials(no_training(ai), num_trainings, num_batches, test_function(strat_rand, 1000), say=speak)
#print(x[:10])
#print(y[:10])
###########################
ai1 = HogAI(q=dict(), alpha=0.25)
print(len(ai1.q))

x, y = trials(train_function(ai1), num_trainings, num_batches, test_function(strat_rand, 1000), say=speak)
print(x[:10])
print(y[:10])
###########################
ai2 = HogAI(q=dict())
print(len(ai2.q))

x, y = trials(train_function(ai2), num_trainings, num_batches, test_function(strat_rand, 1000), say=speak)
print(x[:10])
print(y[:10])
print(ai is ai1 is ai2)
###########################
ai3 = HogAI(q=dict(), alpha=0.75)
print(len(ai3.q))

x, y = trials(train_function(ai), num_trainings, num_batches, test_function(strat_rand, 1000), say=speak)
print(x[:10])
print(y[:10])