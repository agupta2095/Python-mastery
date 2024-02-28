# readport.py

import csv
from pprint import pprint
from collections import Counter, defaultdict
# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio

def read_rides_as_dict(filename):
    records = []
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            dayType = row[2]
            numOfRiders = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': dayType,
                'rides': numOfRiders
            }
            records.append(record)
    return records

def findPeopleOnADate(records, date):
  return sum([1 for s in records if s['date'] == date])

if __name__ == "__main__":
    portfolio = read_portfolio("../Data/portfolio.csv")
    pprint(portfolio)
    pprint([s for s in portfolio if s['shares'] > 100])
    print(sum([s['shares']*s['price'] for s in portfolio]))
    pprint({s['name'] for s in portfolio})

    totals = Counter()
    #It attempts to use a list comprehension for a side effect (updating the totals dictionary) rather than for generating a list
    #pprint([totals[s['name']] += s['shares'] for s in portfolio])
    for s in portfolio:
        totals[s['name']] += s['shares']
    pprint(totals.most_common(2))

    records = read_rides_as_dict("../Data/ctabus.csv")
    print(len(records))
    ##How many bus routes exist in Chicago?
    byRoute = Counter()
    for record in records:
        byRoute[record['route']] += record['rides']
    print("Number of routes = %d" % byRoute.__sizeof__())

    ##Question 2
    rides_route_day = { }
    for record in records:
        rides_route_day[record['route'], record['date']] = record['rides']
    print(rides_route_day['22', '02/02/2011'])
    ##Question 3
    pprint(byRoute)

    ## What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
    dict2001 = Counter()
    dict2011 = Counter()
    for record in records:
        if '2001' in record['date']:
            dict2001[record['route']] += record['rides']
        if '2011' in record['date']:
            dict2011[record['route']] += record['rides']

    diffDict = dict2011 - dict2001
    pprint(diffDict.most_common(5))

    rides_by_year = defaultdict(Counter)
    for row in records:
        year = row['date'].split('/')[2]
        rides_by_year[year][row['route']] += row['rides']

    #Difference in ride counts for each route between the years 2011 and 2001 using Counter objects from the collections module
    diffs = rides_by_year['2011'] - rides_by_year['2001']

    for route, diff in diffs.most_common(5):
        print(route, diff)