with open('input.txt','r') as f:
    a = f.read()

#split the file into a list with each line as an element
map_list = a.splitlines()

#define a function to compute the count of trees in a map with slopes x and y
def tree_count(map_list_local, x, y):           #x is the number of steps to the right, y is number of steps down
    tree = 0
    for i in range(0, len(map_list_local),y):    #iterating through the index numbers of each element in MapList
        m = int(((i/y)*x) % len(map_list_local[i]))     # using the remainder because product would go out of range soon. The given pattern repeats towards the right, so the remainder will give us the correct index number from the start of the pattern
                                                        # using i/y to neutralise the 'steps' in y. Useful in cases where y is more than 1
        if map_list_local[i][m] == '#':
            tree = tree + 1
    return tree

#create a list of tuples with x and y increments from the question
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
tree_product = 1
for i in slopes:        #iterate through the list of tuples/cases and compute the product
    x = i[0]
    y = i[1]
    tree_product = tree_product * tree_count(map_list, x, y)
print(tree_product)

