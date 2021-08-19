#Following are the starting numbers in the memory game

starting_nums = [11,0,1,10,5,19]

#creating a set of nums which have already been 'spoken'
#removing the last starting number from the set so that the subsequent program registers that it was the first time it was used

start_set_list = []
for start_num in starting_nums:
    start_set_list.append(start_num)
start_set_list.pop()

nums_spoken = set(start_set_list)

#creating a list of tuples with these nums and their positions in the list
# we will append subsequent nums along with their positions into this list
enumerated_nums = list(enumerate(starting_nums))



while len(enumerated_nums) < 2020:
    last_num = enumerated_nums[-1][1]

    if last_num not in nums_spoken:
        new_tup = ((enumerated_nums[-1][0] + 1), 0)
        enumerated_nums.append(new_tup)
        nums_spoken.add(last_num)

    else:
        for i in range((len(enumerated_nums) - 2), -1, -1):
            if last_num == enumerated_nums[i][1]:
                next_num = len(enumerated_nums) - (enumerated_nums[i][0]+1)
                new_tup = ((enumerated_nums[-1][0] + 1), next_num)
                enumerated_nums.append(new_tup)
                break
            

print(enumerated_nums[-1])

#this is a very circuitous way of doing this
#we can do away with the set and enumerate list 