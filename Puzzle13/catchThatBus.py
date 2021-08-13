with open('input.txt', 'r') as f:
    a = f.read() 

inp = a.splitlines()

#isolate the timestamp from the input
timestamp = int(inp[0])


#isolate the valid bus numbers into a separate list
buses_str = inp[1]
buses_full_list = buses_str.split(',')

bus_nos = []

for bus in buses_full_list:
    if bus != 'x':
        bus_nos.append(int(bus))

minimum_wait_time = 100000000000   #starting from a really big number that will get replaced by a smaller number found later
earliest_busID = 0

for busID in bus_nos:
    wait_time = busID - (timestamp % busID)
    if wait_time < minimum_wait_time:
        minimum_wait_time = wait_time
        earliest_busID = busID

#compute the required metric
print(earliest_busID * minimum_wait_time)