#pcost.py

import os

def getTotalAmt(filename):
    return sum(int(qty)*float(val) for (qty, val) in (line.split(" ")[1:] for line in open(filename, 'r')))

def getTotalAmount(filename):
    sum = 0.0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    list = line.split(" ")
                    sum += int(list[1])*float(list[2])
                except ValueError as e:
                    print(f'Couldn\'t parse value, reason: {e}')
                except IndexError as e:
                    print(f'Insufficient data: {line}, reason: {e}')
    except FileNotFoundError as fileNotfoundErr:
        print(fileNotfoundErr)
    return sum


if __name__ == '__main__':
    print(getTotalAmount('../Data/portfolio3.dat'))
    print(getTotalAmount('./Data/portfolio.dat'))
    print(getTotalAmt('../Data/portfolio.dat'))