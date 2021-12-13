import pylab

from pyLabExamples import strDollar_to_int

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


def main():
    five_percent_growth_compounded_annually('10,000')


if __name__ == '__main__':
    main()