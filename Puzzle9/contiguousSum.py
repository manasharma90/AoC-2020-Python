with open('input.txt', 'r') as f:
    a = f.read()

input_string = a.splitlines()
input_nums = []

# making a list of all the elements as integers for ease of mathematical operations
for input in input_string:
    input_nums.append(int(input))

# the number from the previous puzzle is 2089807806
# further operation will be done only on the numbers preceeding this in the list

split_index = input_nums.index(2089807806)

working_list = input_nums[:split_index]

# we start adding successive elements from the list starting from index 0 until we get 2089807806
# if sum exceeds 2089807806, we terminate the addition and start adding from the next index number
# after exiting while loop, we need to remove the previously added index value from the checked num list using pop


for i in range(len(working_list)):

    checked_nums = [working_list[i]]

    while sum(checked_nums) <= 2089807806:

        for num in working_list[i+1:]:
            checked_nums.append(num)

            if sum(checked_nums) == 2089807806:
                checked_nums.sort()
                smallest = checked_nums[0]
                largest = checked_nums[-1]
                encryption_weakness = smallest + largest
                print(encryption_weakness)
    
    checked_nums.pop(0)
            
        


        

        



