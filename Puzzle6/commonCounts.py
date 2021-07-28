with open('input.txt', 'r') as f:
    a = f.read()

# split the input file on blank lines ('\n\n') to return group-wise data

forms = a.split('\n\n')

total_intersection = 0


for form in forms:
    persons = form.split('\n')          #split each form into a list of strings representing individual answers
    form_yes_sets = []
    
    for person in persons:
        person_yes = set(person)        #create a set of answers for each person in the group
        if len(person_yes) != 0:
            form_yes_sets.append(person_yes) #validating that there should be at least one answer per individual so that intersection is not zero for blank spaces in the file
    
    yes_intersection = form_yes_sets[0] #starting with the set of the first individual in the group

    for person_set in form_yes_sets:    #sequentially check the intersection of each individual in the group with the intersection of the previous ones
        yes_intersection = yes_intersection.intersection(person_set)
    
    form_intersection_length = len(yes_intersection) #gives the count of the common answers in the group/form

    total_intersection += form_intersection_length #adding the count to the total

print(total_intersection)
    
    



        


    

    



