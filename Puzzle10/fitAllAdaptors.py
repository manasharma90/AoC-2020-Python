with open('input.txt', 'r') as f:
    a = f.read()

input_string = a.splitlines()
adapters = []

# making a list of all the elements as integers for ease of mathematical operations
for input in input_string:
    adapters.append(int(input))

#appending a 0 to the adapters to include the outlet joltage and run the recursive function later
adapters.append(0)

# defining a function to generate a list of valid next joltages for a given joltage
def next_joltages(start_joltage):
    return [start_joltage + 1, start_joltage + 2, start_joltage +3]


start_joltage = 0


#defining a recursive function to determine the viable branch where all the adapters get used
def check_branch(start_list, remaining_adapters, total_adapters):
    start_joltage = start_list[-1]
    if start_joltage in remaining_adapters:
        remaining_adapters_downtree = remaining_adapters.copy()
        remaining_adapters_downtree.remove(start_joltage)
        njs = next_joltages(start_joltage)
        for nj in njs:
            start_list_downstream = start_list.copy()
            start_list_downstream.append(nj)
            returned_list = check_branch(start_list_downstream, remaining_adapters_downtree, total_adapters)
            if len(returned_list) == total_adapters:
                # print("Found the list: ", returned_list)
                return returned_list
    # Return the total viable list
    return start_list[:-1]
        
final_list = check_branch([start_joltage], adapters, len(adapters))


count_diff1 = 0
count_diff2 = 0
count_diff3 = 1 #adding 1 already because we know that the difference between the highest adapter and device is 3

for i in range(1, len(final_list)):
    if final_list[i] - final_list[i-1] == 1:
        count_diff1 += 1
    if final_list[i] - final_list[i-1] == 2:
        count_diff2 += 1
    if final_list[i] - final_list[i-1] == 3:
        count_diff3 += 1

print('Puzzle solution is: ', count_diff1 * count_diff3)

