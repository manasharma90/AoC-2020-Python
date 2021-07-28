with open('input.txt', 'r') as f:
    a = f.read()

# split the input file on blank lines ('\n\n') to return passport data

forms = a.split('\n\n')

#defining a function to create a set containing unique characters from a string
def unique_count(form_string):
    unique_set = set()
    for i in form_string:
        unique_set.add(i)
    return unique_set

#defining a funtion to count the number of 'yes' in a group
#this is the length of the unique_set of each group minus '\n' if there are spaces in the group data
def yes_count(unique_set):
    if '\n' in unique_set:
        count = len(unique_set) - 1
    else:
        count = len(unique_set)
    return count

total_yes_number = 0

for form_string in forms:
    form_yes_number = yes_count(unique_count(form_string))
    total_yes_number= total_yes_number + form_yes_number

print(total_yes_number)