with open ('input.txt', 'r') as f:
    a = f.read()        #reads file as a string
x = a.split()     #splits the file into a list with each word as an element. All elements are strings

numbers = []

for i in x:
    numbers.append(int(i)) #converts each element in list x from str to int
    
for i in range(0, len(numbers)):  #index number loop from the 0th index to the last index in the numbers list
    for x in range(i+1, len(numbers)):   #index number loops from 1st index in the numbers list to the last index in the numbers list
        for m in range(x+1, len(numbers)):
            if numbers[i] + numbers[x] + numbers[m] == 2020:
                print(numbers[i] * numbers[x] * numbers[m])