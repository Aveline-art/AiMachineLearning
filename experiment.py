from train import *

def trials(f, n, groups, test_f, say=lambda x: None):
    assert n % groups == 0, "trials cannot be divided by groups evenly"
    x = [i for i in range(groups + 1)]
    group_size = n // groups
    
    y = []
    model = None
    for i in x:
        say(i)
        model = f(model, group_size)
        result = test_f(model)
        y.append(result)
    
    return [i*group_size for i in x], y

def no_training(ai):
    def f(model, group_size):
        return ai
    return f

def train_function(ai):
    def f(model, group_size):
        if not model:
            return ai
        model = train(model, group_size)
        return model
    return f

def test_function(strat, num_games):
    def f(ai):
        result = test(num_games, ai, strat)
        return result
    
    return f

def speak(x):
    print(f"Now working on batch #{x}", end="\r")


    
