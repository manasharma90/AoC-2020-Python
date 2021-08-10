with open('input.txt', 'r') as f:
    a = f.read()

seats_draft = a.splitlines()
seats = []

for row_string in seats_draft:
    row_list = list(row_string)
    seats.append(row_list)


    
row_length = len(seats[0])


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



def occupied_adjacent(seatList, x, y, rowLength):
    occupied_count = 0
    
    if (y + 1) < rowLength:
        if seatList[x][y + 1] == '#':  #check East
            occupied_count += 1
    else:
        occupied_count += 0

    if (y - 1) >= 0:
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

while True:
    new_seatList = []
    
    for i in range(len(seats)):
        
        new_sublist = []
        for j in range(len(seats[i])):
            if seats[i][j] == 'L' and occupied_adjacent(seats, i, j, row_length) == 0:
                new_sublist.append('#')
                continue
            if seats[i][j] == '#' and occupied_adjacent(seats, i, j, row_length) >= 4:
                new_sublist.append('L')
                continue
            new_sublist.append(seats[i][j])
        new_seatList.append(new_sublist)
    if list_equality(seats, new_seatList):
        break
    seats = new_seatList


occupied_count = 0
 
for row in seats:
    for seat in row:
        if seat == '#':
            occupied_count += 1

print(occupied_count)



    

        





