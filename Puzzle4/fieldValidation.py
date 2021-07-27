

# defining a function to validate the lend of the list
def ValidEntryLength(passport):
    
    if len(passport) == 8:
        return True
    return False

# defining a function to check if the list contains an element that starts with 'cid'
def check_cid(passport):
    for field in passport:
        if field.startswith('cid'):
            return True
    return False

#defining functions to check validity of each field
# Input ["byr", 1231]


def valid_byr(inp):
    if inp[0] == 'byr' and int(inp[1]) >= 1920 and int(inp[1]) <= 2002:
        return True
    return False

def valid_iyr(inp):
    if inp[0] == 'iyr' and int(inp[1]) >= 2010 and int(inp[1]) <= 2020:
        return True
    return False

def valid_eyr(inp):
    if inp[0] == 'eyr' and int(inp[1]) >= 2020 and int(inp[1]) <= 2030:
        return True
    return False

def valid_hgt(inp):
    if inp[0] == 'hgt':
        if inp[1].endswith('cm') and int(inp[1][0:-2]) >= 150 and int(inp[1][0:-2]) <= 193:
            return True
        if inp[1].endswith('in') and int(inp[1][0:-2]) >= 59 and int(inp[1][0:-2]) <= 76:
            return True
    return False

def valid_hcl(inp):
    letters = ['a', 'b', 'c', 'd', 'e', 'f']

    if inp[0] == 'hcl' and len(inp[1]) == 7 and inp[1].startswith('#'):
        for i in inp[1][1:]:
            if not (i in letters or i.isnumeric()):
                return False
        return True

def valid_ecl(inp):
    ecl_types = ['amb','blu','brn','gry','grn','hzl','oth']
    if inp[0] == 'ecl' and inp[1] in ecl_types:
        return True
    return False

def valid_pid(inp):
    nums = list(range(10))
    if inp[0] == 'pid' and len(inp[1]) == 9:
        for i in inp[1]:
            if int(i) not in nums:
                return False
        return True

#defining a function to check if value of the field in input ['field','value'] is valid for that particular field

def valid_all(list):
    a = 0
    
    if (list[0] == 'byr' and valid_byr(list)) or (list[0] == 'iyr' and valid_iyr(list)) or (list[0] == 'eyr' and valid_eyr(list)) or (list[0] == 'hgt' and valid_hgt(list)) or (list[0] == 'hcl' and valid_hcl(list)) or (list[0] == 'ecl' and valid_ecl(list)) or (list[0] == 'pid' and valid_pid(list)):
        a = a + 1
        
    if a > 0:
        return True

#using the above functions in the given input data

with open('input.txt', 'r') as f:
    a = f.read()

# split the input file on blank lines ('\n\n') to return passport data

data = a.split('\n\n')

ValidEntry_length = 0
ValidEntry_cid = 0

for i in data:
    entry = i.split()   #spliting each passport in entry into a list with its 'field:value' as elements
    
    if ValidEntryLength(entry) == True: #check if all entries are present
        b = 0
        for x in entry:
            subEntry = x.split(':')
            
            if valid_all(subEntry):
                b = b + 1
        
        if b == 7:
            ValidEntry_length = ValidEntry_length + 1

    if len(entry) == 7: #check that 'cid' is the *only* entry which is missing
        if check_cid(entry) != True:
            b = 0
            
            for x in entry:
                subEntry = x.split(':')
                
                if valid_all(subEntry):
                        b = b + 1
                if b == 7:
                    ValidEntry_cid = ValidEntry_cid + 1
            
totalValid = ValidEntry_length + ValidEntry_cid
print(totalValid)

       