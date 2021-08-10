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
#Inp: seatList: [[#,L,L,.,.,#],[L,L,L,.,#,#]...]; x = index of first order list (seats); y = index of second order list (rows)
def occupied_adjacent(seatList, x, y, rowLength):
    occupied_count = 0
    
    if (y + 1) < rowLength: #condition to ensure the index doesn't go out of range. The max index possible for each row is (len-1)
        if seatList[x][y + 1] == '#':  #check East
            occupied_count += 1
    else:
        occupied_count += 0

    if (y - 1) >= 0: #condition to ensure the index doesn't become negative and starts iterating from the end of the list
        if seatList[x][y - 1] == '#':  #check West
            occupied_count += 1
    else:
        occupied_count += 0

    if (x - 1) >= 0:
        if seatList[x-1][y] == '#':  #check North
            occupied_count += 1
    else:
        occupied_count += 0

    if (x + 1) < len(seatList):
        if seatList[x + 1][y] == '#':  #check South
            occupied_count += 1
    else:
        occupied_count += 0

    if (x - 1) >= 0 and (y + 1) < rowLength:
        if seatList[x-1][y + 1] == '#':  #check North-East
            occupied_count += 1
    else:
        occupied_count += 0

    
    if (x - 1) >= 0 and (y-1) >= 0:
        if seatList[x-1][y-1] == '#':  #check North-West
            occupied_count += 1
    else:
        occupied_count += 0

    if (x + 1) < len(seatList) and (y + 1) < rowLength:
        if seatList[x + 1][y + 1] == '#':  #check South-East
            occupied_count += 1
    else:
        occupied_count += 0
    
    if (x + 1) < len(seatList) and (y - 1) >= 0:
        if seatList[x + 1][y - 1] == '#':  #check South-West
            occupied_count += 1
    else:
        occupied_count += 0
    
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
            if seats[i][j] == '#' and occupied_adjacent(seats, i, j, row_length) >= 4:
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



    

        





