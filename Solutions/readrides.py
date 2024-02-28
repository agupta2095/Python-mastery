import tracemalloc
import csv
from collections import namedtuple

class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route,
        self.date = date,
        self.daytype = daytype,
        self.rides = rides

def read_rides_as_tuple(filename):
    records = []
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        next(rows) #SKIP headings
        for row in rows:
            route = row[0]
            date = row[1]
            dayType = row[2]
            numberOfRiders = int(row[3])
            record = [route, date, dayType, numberOfRiders]
            records.append(record)
    return records

def read_rides_as_dictionary(filename):
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
                'route' : route,
                'date' : date,
                'daytype': dayType,
                'rides' : numOfRiders
            }
            records.append(record)
    return records

def read_rides_as_class(filename):
    records =[]
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            dayType = row[2]
            numOfRiders = int(row[3])
            newRecord = Row(route, date, dayType, numOfRiders)
            records.append(newRecord)
    return records
RowT = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
def read_rides_as_named_tuple(filename):
    records = []
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            dayType = row[2]
            numOfRiders = int(row[3])
            r = RowT(route=route, date=date, daytype=dayType, rides=numOfRiders)
            records.append(r)
    return records

if __name__ == "__main__":
    tracemalloc.start()
    records = read_rides_as_tuple('../Data/ctabus.csv')
    print("Memory Use Tuple: Current: %.2f MB, Peak: %.2f MB" % (tracemalloc.get_traced_memory()[0]/1024/1024,
                                                           tracemalloc.get_traced_memory()[1]/1024/1024))
    tracemalloc.stop()
    tracemalloc.start()
    records = read_rides_as_dictionary('../Data/ctabus.csv')
    print("Memory Use Dictionary: Current: %.2f MB, Peak: %.2f MB" % (tracemalloc.get_traced_memory()[0]/1024/1024,
                                                                      tracemalloc.get_traced_memory()[1]/1024/1024))
    tracemalloc.stop()
    tracemalloc.start()
    records = read_rides_as_class('../Data/ctabus.csv')
    print("Memory Use Class Object: Current: %.2f MB, Peak: %.2f MB" % (tracemalloc.get_traced_memory()[0]/1024/1024,
                                                                      tracemalloc.get_traced_memory()[1]/1024/1024))
    tracemalloc.stop()
    tracemalloc.start()
    records = read_rides_as_named_tuple('../Data/ctabus.csv')
    print("Memory Use Named Tuple: Current: %.2f MB, Peak: %.2f MB" % (tracemalloc.get_traced_memory()[0]/1024/1024,
                                                                      tracemalloc.get_traced_memory()[1]/1024/1024))
    tracemalloc.stop()

    '''
    Memory Use Tuple: Current: 126.77 MB, Peak: 126.80 MB
    Memory Use Dictionary: Current: 206.09 MB, Peak: 206.12 MB  
    Memory Use Class Object: Current: 192.87 MB, Peak: 192.90 MB
    Memory Use Named Tuple: Current: 122.37 MB, Peak: 122.39 MB
    '''