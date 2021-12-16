import random

import pylab

from pyLabExamples import strDollar_to_int
from PlayDice import rollDie

def five_percent_growth_compounded_annually(principal: str = '100,000', years: int = 20):
    """just do compound interest"""
    # principal = 10000  # initial investment
    principal = strDollar_to_int(principal)
    interest_rate = 0.05
    # years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interest_rate
    pylab.plot(values)              # to plot the image but not show up
    # label axes and title
    pylab.title('5% Growth, Compounded Annually')
    pylab.xlabel('Years of Compounding')
    pylab.ylabel('Value of Principal ($)')
    pylab.savefig('investmentSaved')
    pylab.show()


def checkPascal(numTrials=100000):
    yes = 0.0  # float
    for i in range(numTrials):  # Traverse the numTrials
        for j in range(24):  # Traverse in 24 times.
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                yes += 1
                break
    print ('Probability of losing= ' + str(1.0 - yes/numTrials))


def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/float(numFlips)

def main():
    # >>> to plot five_percent_growth_compounded_annually as below
    # five_percent_growth_compounded_annually('10,000')
    # >>> to run the checkPascal func.
    checkPascal()


if __name__ == '__main__':
    main()