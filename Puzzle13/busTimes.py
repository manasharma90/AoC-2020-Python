#this is a brute force solution to the puzzle which probably works but won't be of use for the given data due to the sheer number of iterations to reach the answer!

with open('input.txt', 'r') as f:
    a = f.read() 

inp = a.splitlines()

#isolate the bus numbers into a separate list
buses_str = inp[1]
buses_full_list = buses_str.split(',')

enumerated_buses = list(enumerate(buses_full_list))

valid_buses = []

for enumerated_bus in enumerated_buses:
    if enumerated_bus[1] != 'x':
        valid_buses.append(enumerated_bus)
#now we have a list of valid buses with elements in a tuple (offset, 'busID')

#defining a fuction to compute the departure time for each bus from a given timestamp
def bus_departure(start_timestamp, busID):
    departure = (busID - (start_timestamp % busID)) + start_timestamp
    return departure

#isolating the list of offsets from the tuples to have a comparator for the while loop exit condition
given_offsets = []
for valid_bus in valid_buses:
    given_offsets.append(valid_bus[0])

#creating a test list of the offsets computed after each iteration
#already starting with 0 (ie. offset of the 1st element) because we are iterating from index 1
test_offsets = [0]

#defining exit condition
def list_equality(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            return True
        else:
            return False

#earliest timestamp given in the puzzle
earliest_timestamp = 100000000000000

while True:
   
    test_offsets = [0]

    for i in range(1, len(valid_buses)):
        print('checking busID: ', valid_buses[i][1])
        offset = bus_departure(earliest_timestamp, int(valid_buses[i][1])) - earliest_timestamp
        print('calculated offset: ', offset)
        if offset == valid_buses[i][0]:
            test_offsets.append(offset)
            print(test_offsets)
            continue
        else:
            break
    if list_equality(given_offsets, test_offsets):
        break
    earliest_timestamp += 1
    test_offsets = [0]

print( earliest_timestamp)
