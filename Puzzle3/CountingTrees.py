with open('input.txt','r') as f:
    a = f.read()

#split the file into a list with each line as an element
MapList = a.splitlines()

tree = 0

for i in range(0, len(MapList)):    #iterating through the index numbers of each element in MapList
    m = (i*3) % len(MapList[i])     # using the remainder because product would go out of range soon. The given pattern repeats towards the right, so the remainder will give us the correct index number from the start of the pattern

    if MapList[i][m] == '#':
        tree = tree + 1
print(tree) 
