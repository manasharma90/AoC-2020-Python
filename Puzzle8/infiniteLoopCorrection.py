with open('input.txt', 'r') as f:
    a = f.read()

instructions = a.splitlines()
instructions_list = []

import re

#creating a list of tuples (code, value) from the instructions using regex
for instruction in instructions:
    instr_pattern =re.compile(r'(\w+)\s(.*)$')
    matched_instr  = instr_pattern.search(instruction)

    if matched_instr:
        
        code = matched_instr.group(1)
        value = matched_instr.group(2)
        instructions_list.append((code, int(value)))

# defining a function to check if the loop is infinite
# function returns a tuple (True/False , acc_count)

def check_infinite(instructions_list):
    acc_count = 0
    completed_indices = []
    i = 0

    # Using while loop to continue iteration until an index is reached for a second time. 
    # The completed index is appended to the completed_indices list with eah condition
    # The value of i is increased at the *end* of each condition
    # It is necessary to use continue at the end of each condition so that the while loop iterates through the new value of i

    while i not in completed_indices and i < len(instructions_list):
        if instructions_list[i][0] == 'nop':
            completed_indices.append(i)
            i += 1
            
            continue
        
        if instructions_list[i][0] == 'acc':
            completed_indices.append(i)
            acc_count += instructions_list[i][1]
            i += 1
            
            continue
        
        if instructions_list[i][0] == 'jmp':
            completed_indices.append(i)
            i += instructions_list[i][1]
            
            continue
    
    if i != len(instructions_list):
        return (True, acc_count)
    
    else:
        return (False, acc_count)
        
# creating a list of index numbers where tuples with nop and jump occur in the instructions list

nop_index_list = []
jmp_index_list = []

# using enumerate function to enumerate the pair of (index num, element) in the list
# append those index nums which have 'nop' or 'jmp' as element

for i, instruction_tup in enumerate(instructions_list):
    if instruction_tup[0] == 'nop':
        nop_index_list.append(i)

for i, instruction_tup in enumerate(instructions_list):
    if instruction_tup[0] == 'jmp':
        jmp_index_list.append(i)

# creating a copy of the instructions list within the for loop so that the nop/jmp gets replaced in the copy with each iteration
# this ensures that only nop/jmp is changed in the list one-by-one and go back to the original state once checked
for nop_index in nop_index_list:
    instructions_list_copy = instructions_list.copy()
    old_tup = instructions_list_copy[nop_index]
    new_tup = ('jmp', old_tup[1])       #need to create a new tuple with the replaced value beccause tuple object doesn't support item assignment
    instructions_list_copy[nop_index] = new_tup
    
    is_infinite, acc_count = check_infinite(instructions_list_copy)
    if not is_infinite: #ie. if check_infinite[0] is False
        print(acc_count)

for jmp_index in jmp_index_list:
    instructions_list_copy = instructions_list.copy()
    old_tup = instructions_list_copy[jmp_index]
    new_tup = ('nop', old_tup[1])
    instructions_list_copy[jmp_index] = new_tup
    
    is_infinite, acc_count = check_infinite(instructions_list_copy)
    if not is_infinite:
        print(acc_count)

        
