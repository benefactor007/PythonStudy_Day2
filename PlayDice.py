# coding=utf-8

import random

def rollDie() -> int:
    """return a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def testRoll(n: int = 10):
    result = ""
    for i in range(n):
        result = result + str(rollDie())
    print(result)


def main():
    testRoll()



if __name__ == '__main__':
    main()