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
        #'1 drab red bag, 4 clear crimson bags, 6 plain fuchsia bags' etc.
        # it may even be 'no other bags'
        # we now use another regex to isolate the two colour words after the digit-space and before the , or . or space

       
        v_pattern = re.compile(r'(\d+\s[a-z]+\s[a-z]+)')  #pattern of a digit and 2 words
        v_matched = v_pattern.match(v_all)

        v_tups = []     #creating a blank list outside of the if condition. So those values which do not match the pattern (ie. 'no other bags') will generate a blank list only
        if v_matched:
            v_list = re.findall(v_pattern, v_all)
            for value in v_list:
                count = value[:1]  #separates the digit from the colour. Would be challenging if the count is more than 1 digit
                colour = value[2:]
                v_tups.append((colour, int(count)))

        rules_dict.update({k:v_tups}) #updates the dict with k:v eg. 'bright black' : [('shiny orange':5), ('wavy tan':2), ('shiny yellow':3)]

def bags_in_colour(colour, count, colour_dict):
    bag_tups = colour_dict.get(colour)

    if len(bag_tups) == 0:  #base case for 'no other bag' bag_tups is a blank list, hence len is 0
        print("completed leaf: " + colour)
        return count
    
    total = 0
    for (sub_colour, sub_count) in bag_tups:  #if there are more bags within the colour, then recurive function is initiated on the sub colour
        print("adding " + sub_colour + ":" + str(sub_count))
        total += bags_in_colour(sub_colour, sub_count, colour_dict)
    
    print("completed branch: " + colour)
    print("total of branch = " + str((total * count) + count))
    return (total * count) + count # + count is needed to add the bag itself

print((bags_in_colour("shiny gold", 1, rules_dict))-1) #-1 done at the end to remove the outermost shiny gold bag from the count                                                              