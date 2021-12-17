import random
import math
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
    pylab.plot(values)  # to plot the image but not show up
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
    print('Probability of losing= ' + str(1.0 - yes / numTrials))


def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads / float(numFlips)


def flipPolt(minExp, maxExp):  # Exp = exponent
    ratios = []
    diffs = []
    xAxis = []  # List of observed sample quantities
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)  # set the each of given sample population, it's 2 as the base.
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):  # to get the number of Heads
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads  # to get the number of Tails
        if numTails != 0:
            ratios.append(numHeads / float(numTails))  # warning: the division by 0 is not defined
        else:
            print("WARNING: The fraction is zero")
            ratios.append(float('inf'))
        diffs.append(abs(numHeads - numTails))
    print("The list of ratios:", ratios)
    print("The list of diffs:", diffs)
    print("The list of xAxis:", xAxis)
    # Let's try to make a plot for each one.
    pylab.title("Difference Between Heads and Tails")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Abs(#Heads - #Tails)")
    pylab.plot(xAxis, diffs)
    pylab.figure()
    pylab.title("Heads/Tails Ratios")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Heads/Tails")
    pylab.plot(xAxis, ratios)
    pylab.figure()
    pylab.title("Difference Between Heads and Tails")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Abs(#Heads - #Tails)")
    pylab.plot(xAxis, diffs,'bo')
    # This quote "bo" says, don't connect it by line \
    # but just put a dot as an "o" and B says, make it blue.
    pylab.semilogx()
    # PyLab.semilogx says make the x-axis logarithmic
    pylab.semilogy()
    # the reason why we make X-axis and Y-axis both logarithmic, Because both have a \
    # large range, and by making it logarithmic, I can see what's happening at the left side \
    # in this case where things are changing.
    pylab.figure()
    pylab.plot(xAxis,ratios,'ro')
    pylab.title("Heads/Tails Ratios")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Heads/Tails")
    pylab.semilogx()
    # For the ratios, the y-axis does not have a very large range.


def main():
    # >>> to plot five_percent_growth_compounded_annually as below
    # five_percent_growth_compounded_annually('10,000')
    # >>> to run the checkPascal func.
    # checkPascal()
    # >>> to run the flipPlot func.
    flipPolt(4, 20)
    pylab.show()


if __name__ == '__main__':
    main()
