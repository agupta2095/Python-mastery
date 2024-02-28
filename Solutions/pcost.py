#pcost.py

## This code can get too many value to unpack error if the line.split(" ")[1:] produces more than 2 values
def portfolio_cost(filename):
    try:
        with open(filename, 'r') as file:
            return sum(float(price)*int(qty) for (qty, price) in (line.split(" ")[1:] for line in file))
    except FileNotFoundError as err:
        print(f'File not found {err}')
    except ValueError as err:
        print(f'Value cannot be parsed {err}')
    except Exception as exception:
        print(f'An unknown error occured: {exception}')
    return 0.0

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
    #print(getTotalAmount('../Data/portfolio3.dat'))
    print(getTotalAmount('../Data/portfolio2.dat'))
    print(getTotalAmt('../Data/portfolio2.dat'))
    print(portfolio_cost('../Data/portfolio2.dat'))