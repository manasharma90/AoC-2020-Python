# defining a function to execute binary partitioning of a list
# input = list; output = tuple with two lists ie. ([first half list], [second half list])
def list_half(input_list):
    half = len(input_list)//2
    lower_half = input_list[:half]
    upper_half = input_list[half:]
    return lower_half, upper_half



with open('input.txt', 'r') as f:
    a = f.read()

boarding_passes = a.split('\n')

#cleaning the file by validating that the elements are 10 characters and each character is either F,B,R or L
boarding_passes_cleaned = []
for bp in boarding_passes:
    if len(bp) == 10:
        valid = True
        for l in bp:
            if l not in ['F', 'B', 'R', 'L']:
                valid = False
        if valid:
            boarding_passes_cleaned.append(bp)


#defining a function to decode the row number from the boarding pass code
def decode_row(bp_code):
    rows = list(range(128))

    for letter in bp_code:
        
        if letter == 'F':
            rows = list_half(rows)[0]
        if letter == 'B':
            rows = list_half(rows)[1]
    return rows[0]

#defining a function to decode the column number from the boarding pass code
def decode_column(bp_code):
    columns = list(range(8))

    for letter in bp_code:
        
        if letter == 'L':
            columns = list_half(columns)[0]
        if letter == 'R':
            columns = list_half(columns)[1]
    return columns[0]

# generating a list of seat IDs (sorted in ascending order) of the boarding passes in the file
seat_ids = []
for bp_code in boarding_passes_cleaned:
    r = decode_row(bp_code)
    c = decode_column(bp_code)
    sID = (r * 8) + c
    seat_ids.append(sID)
seat_ids.sort()

# Finding out the 'missing' seat ID ie. which ID has been skipped 
# difference between two successive IDs in the list will be 2 in this case
for i in range(len(seat_ids)-1):
    if (seat_ids[i+1] - seat_ids[i]) == 2:
        print(seat_ids[i], seat_ids[i+1])
        break; #'break' is to optimize the code. The loop will stop the moment the if condition is fulfilled