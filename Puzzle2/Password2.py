with open ('input.txt', 'r') as f:
    a = f.read()

list1 = a.splitlines()  #creates a list with each line of the file as an element

x = 0       # xth position in the password
y = 0       # yth position in the password
z = ''      # character to be checked
m = ''      # password to be checked against
total = 0   # total number of valid passwords

for i in list1:
    list2 = i.split()           #each element of list1 is split at spaces. Yeilds a list with element ['x-y','z:','m']
    z = list2[1][0]             # the 0th index of the string in first index place of list 2. Removes the : at the end of 'z:'
    m = list2[2]                # password is the 2nd index of list2
    list3 = list2[0].split('-') #the 0th index of list2 ('x-y') is further split with '-' as a separator. Generates a list with ['x','y']
    x = int(list3[0]) - 1           # integer form of the 0th index of list3 minus 1 ('no zero index')
    y = int(list3[1]) - 1           # integer form of the 1st index of list3 minus 1 ('no zero index')

    if (m[x] == z or m[y] == z) and (m[x] != m[y]): # validity condition. 'or' is true even if both conditions are true, so need to remove the 'extra' passwords where both positions are occupied by z
        total = total + 1

print(total)