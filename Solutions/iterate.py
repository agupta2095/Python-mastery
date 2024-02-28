from collections import defaultdict, Counter
import csv
from pprint import pprint
import tracemalloc

def read_rides_as_dictionary(filename):
    records = []
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record2 = dict(zip(headers, row))
            records.append(record2)
    return records


if __name__ == "__main__":
    records = read_rides_as_dictionary("../Data/portfolio.csv")
    pprint(records)
    byname = defaultdict(list)
    for name, *data in records:
        byname[name].append(data)

    pprint(byname['IBM'])
    for rowno, record in enumerate(records):
        print(rowno, record)

    headers = ['name', 'shares', 'price']
    for record in records:
        record2 = dict(zip(headers, record))
        print(record2)

    s = ('GOOG', 100, 490.10)
    s1 = ','.join(str(x) for x in s)
    print(s1)
    tracemalloc.start()
    #rows = read_rides_as_dictionary("../Data/ctabus.csv")
    f = open('../Data/ctabus.csv')
    f_csv = csv.reader(f)
    headers = next(f_csv)
    rows = (dict(zip(headers, row)) for row in f_csv)
    rt22 = [row for row in rows if row['route'] == '22']

    max22 = max(rt22, key=lambda row: int(row['rides']))
    print(max22)
    y_list_comprehension = (tracemalloc.get_traced_memory()[0]/1024/1024)
    print("%.3f MB memory used" % y_list_comprehension)
    tracemalloc.stop()

    ###USING GENERATOR
    tracemalloc.start()
    f = open('../Data/ctabus.csv')
    f_csv = csv.reader(f)
    headers = next(f_csv)
    rows = (dict(zip(headers, row)) for row in f_csv)
    rt22 = (row for row in rows if row['route'] == '22')
    max22 = max(rt22, key=lambda row: int(row['rides']))
    print(max22)
    y_generator = (tracemalloc.get_traced_memory()[0] / 1024 / 1024)
    print("%.3f MB memory used" % (tracemalloc.get_traced_memory()[0] / 1024 / 1024))
    tracemalloc.stop()
    print ("%.10f" % (y_list_comprehension//y_generator)) ## 81 times less memory consumed


