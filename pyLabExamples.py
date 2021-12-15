import pylab
import string

"""Please use 'pip install matplotlib' to install PyLab"""


def class_example1():
    pylab.plot([1, 2, 3, 4], [1, 2, 3, 4])
    pylab.plot([1, 4, 2, 3], [5, 6, 7, 8])
    pylab.show()  # only execute pylab.show() once per program.
    """The program will stop running, essentially"""


def class_example2():
    pylab.figure(1)
    pylab.plot([1, 2, 3, 4], [1, 2, 3, 4])
    pylab.figure(2)
    pylab.plot([1, 4, 2, 3], [5, 6, 7, 8])
    pylab.savefig('firstSaved')
    pylab.figure(1)
    pylab.plot([5, 6, 7, 10])
    pylab.savefig('secondSaved')
    pylab.show()


def strDollar_to_int(strDollar: str = '10,000,000') -> int:
    """Tran"""
    # print(strDollar)
    # word_len = len(strDollar)
    result = ""
    while ',' in strDollar:
        first_engage = str.index(strDollar, ",")
        rest_part = strDollar[first_engage + 1:]
        result += strDollar[:first_engage]
        # print(rest_part)
        strDollar = rest_part
    print(result + rest_part)
    return int(result + rest_part)


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
    pylab.plot(values)
    # label axes and title
    pylab.title('5% Growth, Compounded Annually')
    pylab.xlabel('Years of Compounding')
    pylab.ylabel('Value of Principal ($)')
    pylab.savefig('investmentSaved')
    pylab.show()


def main():
    # class_example1()
    # class_example2()
    # five_percent_growth_compounded_annually(10)
    five_percent_growth_compounded_annually('10,000')

# class TestRoll():






if __name__ == '__main__':
    main()
