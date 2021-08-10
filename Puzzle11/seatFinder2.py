with open('input.txt', 'r') as f:
    a = f.read()

seats_draft = a.splitlines()
seats = []

#creating a list with elements as a list of rows
for row_string in seats_draft:
    row_list = list(row_string)
    seats.append(row_list)


# determining length of each row in the pattern. 
# Each row is of equal size and each element of the list 'seats' represents a row
# Hence row length will be the len of any element within the list 'seats'   
row_length = len(seats[0])

#Defining a function to check if two lists are exactly the same
#Since we are dealing with two dimensional arrays, the function checks the equality of both levels
def list_equality(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(0,len(list1)):
        if len(list1[i]) != len(list2[i]):
            return False
        
        for j in range(0,len(list1[i])):
            if list1[i][j] == list2[i][j]:
                continue
            else:
                return False
    return True

#Using two dimensional arrays to determine the occupied seats
#Inp: seatList: [[#,L,L,.,.,#],[L,L,L,.,#,#]...]; x = index of first order list (seats ie. north/south); y = index of second order list (rows ie. east/west)
def occupied_adjacent(seatList, x, y, rowLength):
    occupied_count = 0
    
    #checking east
    for e in range((y+1), rowLength):
        if seatList[x][e] == '.':
            continue
        if seatList[x][e] == '#':
            occupied_count += 1
            break
        if seatList[x][e] == 'L':
            break
    
    #checking west
    for w in reversed(range(y)):
        if seatList[x][w] == '.':
            continue
        if seatList[x][w] == '#':
            occupied_count += 1
            break
        if seatList[x][w] == 'L':
            break
    
    #checking north
    for n in reversed(range(x)):
        if seatList[n][y] == '.':
            continue
        if seatList[n][y] == '#':
            occupied_count += 1
            break
        if seatList[n][y] == 'L':
            break
    
    #checking south
    for s in range((x+1), len(seatList)):
        if seatList[s][y] == '.':
            continue
        if seatList[s][y] == '#':
            occupied_count += 1
            break
        if seatList[s][y] == 'L':
            break
    
    #checking north-east
    i = 1
    while (y+i) < rowLength and (x-i) >= 0:
        if seatList[x-i][y+i] == '.':
            i += 1
            continue
        if seatList[x-i][y+i] == '#':
            occupied_count += 1
            break
        if seatList[x-i][y+i] == 'L':
            break
        
    #checking north-west
    i = 1
    while (y-i) >= 0 and (x-i) >= 0:
        if seatList[x-i][y-i] == '.':
            i += 1
            continue
        if seatList[x-i][y-i] == '#':
            occupied_count += 1
            break
        if seatList[x-i][y-i] == 'L':
            break

    #checking south-east
    i = 1
    while (y+i) < rowLength and (x+i) < len(seatList):
        if seatList[x+i][y+i] == '.':
            i += 1
            continue
        if seatList[x+i][y+i] == '#':
            occupied_count += 1
            break
        if seatList[x+i][y+i] == 'L':
            break
    
    #checking south-west
    i = 1
    while (y-i) >= 0 and (x+i) < len(seatList):
        if seatList[x+i][y-i] == '.':
            i += 1
            continue
        if seatList[x+i][y-i] == '#':
            occupied_count += 1
            break
        if seatList[x+i][y-i] == 'L':
            break

    return occupied_count

new_seatList = []

#using a while loop to keep the code running till a matching pattern emerges
while True:
    new_seatList = [] #duplicating this within the loop as well to ensure that we present a blank list everytime
    
    for i in range(len(seats)):
        
        new_sublist = [] #this will be the new row list within the new seat list
        for j in range(len(seats[i])):
            if seats[i][j] == 'L' and occupied_adjacent(seats, i, j, row_length) == 0:
                new_sublist.append('#')
                continue
            if seats[i][j] == '#' and occupied_adjacent(seats, i, j, row_length) >= 5:
                new_sublist.append('L')
                continue
            new_sublist.append(seats[i][j])
        new_seatList.append(new_sublist) #appending the new row list as an element to the new seat list
    if list_equality(seats, new_seatList): #executing break condition ie. when the new and the old seat list are equal
        break
    seats = new_seatList #if no equality, the 'old' seat list gets replaced by the new list compiled during this iteration of the loop
    #In the next iteration of the while loop, the new seat list will again be blank and the 'old' list (seats) will be the list compiled in the previous iteration

#calculting the number of occupied seats when the pattern stabilizes
occupied_count = 0
 
for row in seats:
    for seat in row:
        if seat == '#':
            occupied_count += 1

print(occupied_count)  