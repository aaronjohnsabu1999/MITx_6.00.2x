import random, pylab

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, numBins)
    if title:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
    
                    
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longestRun = []
    for i in range(numTrials):
        rolls = []
        runs  = []
        run   = 1
        for j in range(numRolls):
            rolls.append(die.roll())
            if j != 0:
                if rolls[-1] == rolls[-2]:
                    run += 1
                else:
                    runs.append(run)
                    run = 1
        runs.append(run)
        longestRun.append(max(runs))
    makeHistogram(longestRun, 10, "Run", "Longest Runs", "Histogram of Longest Runs")
    return round(float(sum(longestRun))/numTrials, 3)

print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))