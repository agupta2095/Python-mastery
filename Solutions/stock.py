#stock.py
import pcost
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price

if __name__ == "__main__":
    s = Stock('Goog', 234, 412.3)
    print(s.cost())
    t = Stock('IBM', 50, 91.5)
    print(f'Stock Name: {t.name}, Total Value: {t.cost()}')
    print(pcost.getTotalAmount('../Data/portfolio2.dat'))
