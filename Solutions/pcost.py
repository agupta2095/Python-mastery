#pcost.py

import os

def getTotalAmount(filename):
    sum = 0
    with open(filename, 'r') as file:
        for line in file:
            list = line.split(" ")
            sum += float(list[1])*float(list[2])
    return sum


if __name__ == '__main__':
    print(getTotalAmount('../Data/portfolio.dat'))