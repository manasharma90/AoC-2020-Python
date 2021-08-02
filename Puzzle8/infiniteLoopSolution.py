with open('input.txt', 'r') as f:
    a = f.read()

instructions = a.splitlines()
instructions_list = []

import re

for instruction in instructions:
    instr_pattern =re.compile(r'(\w+)\s(.*)$')
    matched_instr  = instr_pattern.search(instruction)

    if matched_instr:
        
        code = matched_instr.group(1)
        value = matched_instr.group(2)
        instructions_list.append((code, int(value)))

acc_count = 0
completed_indices = []
i = 0

while i not in completed_indices:
    if instructions_list[i][0] == 'nop':
        completed_indices.append(i)
        print('found nop on instruction:', i)
        i += 1
        
        continue
    
    if instructions_list[i][0] == 'acc':
        print('found acc on instruction:', i)
        completed_indices.append(i)

        acc_count += instructions_list[i][1]
        i += 1
        print('ac count: ', acc_count)
        continue
    
    if instructions_list[i][0] == 'jmp':
        completed_indices.append(i)
        print('found jmp on instruction:', i)
        i += instructions_list[i][1]
        print('new index: ', i)
        
        continue

print(acc_count)

    


