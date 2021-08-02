with open('input.txt', 'r') as f:
    a = f.read()

input_string = a.splitlines()
input_nums = []

# making a list of all the elements as integers for ease of mathematical operations
for input in input_string:
    input_nums.append(int(input))

#splitting the original input list into a preamle list of 1st 25 elements and a working list of the rest of the elements
preamble = input_nums[:25]
next_nums = input_nums[25:]


for next_num in next_nums:
    break_outer = True
    from itertools import combinations

    #creating a list of combinations of two numbers from the preamble list

    comb_list = list(combinations(preamble, 2))
    
    # checking condition for each combination pair in the list
    # if the condition is true, we continue the loops and add the next num while removing the first num in the preamble list
    # if the condition is false for any number, we break the outer for loop at that number

    for comb in comb_list:
        

        if sum(comb) == next_num and comb[0] != comb[1]:
            break_outer = False
            
    
    if break_outer:
        print('no combination for',next_num )
        break
    
    preamble.append(next_num)
    preamble.pop(0)
    



