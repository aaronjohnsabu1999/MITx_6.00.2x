import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    pRep = 1.0 - float(CURRENTRABBITPOP)/MAXRABBITPOP

    if CURRENTRABBITPOP > 10:
        CURRENTRABBITPOP += int(CURRENTRABBITPOP * pRep * random.random())
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    pRep = 1.0 - float(CURRENTRABBITPOP)/MAXRABBITPOP
    pEat = float(CURRENTRABBITPOP)/MAXRABBITPOP

    if CURRENTRABBITPOP > 10:
        CURRENTRABBITPOP += int(CURRENTRABBITPOP * pRep * random.random())
        eatenRabbits      = int(CURRENTFOXPOP * random.random() * pEat)

        CURRENTRABBITPOP -= eatenRabbits
        # CURRENTFOXPOP    -= int((CURRENTFOXPOP-eatenRabbits) * random.random()/10)    # Original
        CURRENTFOXPOP    -= int((CURRENTFOXPOP-eatenRabbits) * random.random() * 9/10)  # Problem 8-6
        CURRENTFOXPOP    += int(eatenRabbits * random.random()/3)
        
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    rabbit_populations = []
    fox_populations    = []
    
    rabbitGrowth()
    rabbit_populations.append(CURRENTRABBITPOP)
    fox_populations.append(CURRENTFOXPOP)
    for i in range(numSteps - 1):
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    return (rabbit_populations, fox_populations)

numSteps = 200
(rabbits, foxes) = runSimulation(numSteps)

pylab.plot(rabbits)
pylab.plot(foxes)
pylab.show()

coeffR = pylab.polyfit(range(len(rabbits)), rabbits, 2)
coeffF = pylab.polyfit(range(len(foxes)), foxes, 2)
pylab.plot(pylab.polyval(coeffR, range(len(rabbits))), 'r')
pylab.plot(pylab.polyval(coeffF, range(len(foxes))), 'b')
pylab.show()

pylab.show()