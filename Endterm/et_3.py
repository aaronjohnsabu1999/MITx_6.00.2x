import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    numEqPicks = 0
    for i in range(numTrials):
        initConfig = ['R' for i in range(4)]
        initConfig.extend(['G' for i in range(4)])
        pick = []
        for i in range(3):
            presentPick = random.randint(0, len(initConfig)-1)
            pick.append(initConfig[presentPick])
            initConfig.remove(initConfig[presentPick])
        if pick[0] == pick[1] and pick[1] == pick[2]:
            numEqPicks += 1
    return float(numEqPicks)/numTrials

print(drawing_without_replacement_sim(1))
print(drawing_without_replacement_sim(10))
print(drawing_without_replacement_sim(100))
print(drawing_without_replacement_sim(1000))
print(drawing_without_replacement_sim(10000))
