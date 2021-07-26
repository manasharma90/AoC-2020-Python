with open('input.txt', 'r') as f:
    a = f.read()

# split the input file on blank lines ('\n\n') to return passport data

data = a.split('\n\n')

ValidEntry_length = 0
ValidEntry_cid = 0

# defining a function to validate the lend of the list
def ValidEntryLength(list):
    
    if len(list) == 8:
        return True

# defining a function to check if the list contains an element that starts with 'cid'
def check_cid(list):
    for m in list:
        if m.startswith('cid'):
            return True

for i in data:
    entry = i.split()   #spliting each passport in entry into a list with its 'field:value' as elements
    if ValidEntryLength(entry) == True: #check if all entries are present
        ValidEntry_length = ValidEntry_length + 1
    
    if len(entry) == 7: #check that 'cid' is the *only* entry which is missing
        if check_cid(entry) != True:
            ValidEntry_cid = ValidEntry_cid + 1

totalValid = ValidEntry_length + ValidEntry_cid
print(totalValid)