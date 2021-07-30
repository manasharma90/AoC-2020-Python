with open('input.txt','r') as f:
    a = f.read()

rules = a.split('\n')
rules_dict = {}
    
import re

for rule in rules:
    format_pattern = re.compile(r'(\w+\s\w+)\sbags\scontain\s(.*)\.$') 
    
    matched_rule = format_pattern.search(rule)
    if matched_rule:  
        
        k = matched_rule.group(1) 
        v_all = matched_rule.group(2)

        # key is the first group of regex which are the two colour words (eg. shiny gold) before 'bags contain'
        # group 2 is rest of the string after contain-space  
        #'1 drab red, 4 clear crimson, 6 plain fuchsia' etc.
        # it may even be 'no other bags'
        # we now use another regex to isolate the two colour words after the digit-space and before the , or . or space

       
        v_pattern = re.compile(r'[a-z]+\s[a-z]+') #using [a-z] instead of \w because it considers the digit-space-word as valid otherwise

        v = re.findall(v_pattern, v_all) #generates a list of all the matched patterns. eg: ['drab red', 'clear crimson', 'plaid fuchsia']
        
        rules_dict.update({k:v}) #updates the dict with k:v eg. 'bright black' : ['shiny orange', 'wavy tan', 'shiny yellow']


#defining a function to return a list of keys which have a particular colour in their value list   
def colour_key(colour, colours_dict):
    matches = []
    for (k,v) in colours_dict.items():
        if colour in v:
            matches.append(k)
    return matches


start_colour = 'shiny gold'
colours_checked = set() #creating a checked colour set (unique values) so that we know when to exit the loop ie. when all possible colours get checked

possible_bags = set(colour_key(start_colour, rules_dict)) #possible bags is a set of all keys which have a particular colour in their value list
colours_checked.add(start_colour) #starting with the first colour

while len(possible_bags.difference(colours_checked)) != 0: #we need to continue the loop till the checked bags set becomes equal to the possible bags set ie. the difference between the two is zero
    
    # 1 Iteration
    possible_bags_copy = possible_bags.copy() #creating a copy because the loop would otherwise update the set on which it is being run - error
    for colour in possible_bags_copy:
        if colour not in colours_checked: #running the loop only for those colours which have not yet been checked
            possible_bags.update(set(colour_key(colour, rules_dict))) #updating the set of possible bags
            colours_checked.add(colour) #adding the colour to the set of colours checked
    
print(len(possible_bags)) #len will give the number of items in the possible bags set

