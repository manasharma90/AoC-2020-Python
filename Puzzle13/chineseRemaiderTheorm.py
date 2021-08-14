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

print(valid_buses)
#now we have a list of valid buses with elements in a tuple (offset, 'busID')
#we will now apply the chinese remainder theorm where the offset is the remainder and busID is modulus/divisor
#isolating the list of remainders/offsets (ie. a) and divisors/busIDs (ie. n)

offsets = []
BusIDs = []
bus_minus_offset = [] #not sure why, but this got the right answer

for valid_bus in valid_buses:
    offsets.append(valid_bus[0])
    BusIDs.append(int(valid_bus[1]))
    busDiff = int(valid_bus[1]) - valid_bus[0]
    bus_minus_offset.append(busDiff)


# Using a code from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
 
 
if __name__ == '__main__':
    n = BusIDs
    a = bus_minus_offset
    print(chinese_remainder(n, a))
