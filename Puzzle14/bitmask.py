with open('input.txt', 'r') as f:
    a = f.read()


#preping the input data to finally create a clean list with first element as the mask and subsequent elements as 'mem[num] = decimal value'
#all elements are kept as strings so that leading zeros in 36 but mask code can be incorporated

programs_raw = a.split('mask = ')
raw_strings_programs = []

for i in range(1, len(programs_raw)):
    raw_strings = []
    raw_strings.append(programs_raw[i])
    raw_strings_programs.append(raw_strings)

programs = []

for i in range(len(raw_strings_programs)):
    for j in range(len(raw_strings_programs[i])):
        raw_list_program = raw_strings_programs[i][j].split('\n')
        raw_list_program.pop()
        programs.append(raw_list_program)

# at the end of this we have a list in the form of [['001X11X1X010X1X1010XX10X100101011000', 'mem[43398] = 563312', 'mem[51673] = 263978', 'mem[18028] = 544304215'], 
# ['X0100001101XX11100010XX110XX11111000', 'mem[24151] = 2013', 'mem[15368] = 19793', 'mem[45005] = 478', 'mem[1842] = 190808161', 'mem[36033] = 987', 'mem[26874] = 102']...]

# defining a function to convert decimal integer into a 36 bit binary 'string'

def binary_convert(decimal):
    binary_string_backwards = ''
    dividend = decimal
    while len(binary_string_backwards) <= 35:
        quotient = int(dividend/2)
        remainder = dividend % 2
        binary_string_backwards += str(remainder)
        dividend = quotient
    
    binary_string = ''.join(reversed(binary_string_backwards))
    return binary_string

# defining a function to back convert a binary 'string' into a decimal value
# we will input the unmasked/decoded binary string into this function

def decimal_convert(binary_string):
    positions_list= []
    for i in reversed(range(36)):
        position = 2**i
        positions_list.append(position)
    decimal = 0

    for i in range(len(binary_string)):
        if int(binary_string[i]) != 0:
            decimal += positions_list[i]

    return decimal

# defining a function that will take input in form of ['mask', 'mem[1] = 123', 'mem[2] = 234', 'mem[3] = 345']
# the function will unmask each value of mem[] using the provided instruction
# the function will return a dictionary with keys = mem[1], mem[2].. and values as corresponding unmasked decimal number
 
def unmask_program(program_list):
    mask = program_list[0]

    decoded_dict = {}

    for i in range(1, len(program_list)):
        split_instruction = program_list[i].split(' = ')
        k = split_instruction[0]
        decimal_string_value = split_instruction[1]
        binary_string_value = binary_convert(int(decimal_string_value))
        decoded_binary_string = ''

        for i in range(len(mask)):
            if mask[i] == 'X':
                decoded_binary_string += binary_string_value[i]
                continue
            if mask[i] == '1':
                decoded_binary_string += '1'
                continue
            if mask[i] == '0':
                decoded_binary_string += '0'
                continue

        decimal_val = decimal_convert(decoded_binary_string)
        v = decimal_val
        decoded_dict.update({k : v})
    
    return decoded_dict

# In the question, the values of mem[] get overwritten in the memory
#so we update a blank dictionary with the k,v obtained after unmasking each program
# this will ensure that an key (mem[]) repeated in a subsequent program in the master list will get overwritten
memory = {}

for program in programs:
    memory.update(unmask_program(program))

#adding the values in the dictionary to obtain the required metric
memory_values = memory.values()
total = sum(memory_values)

print(total)


    
    
    
