
#creating a class Ferry with x,y coordinates = 0,0 and direction = 90 
# x,y coordinates will be used to determine the distance travelled
# direction will be used to determine which direction the ferry faces. 
# North = 0, East = 90, South = 180, West = 270

class Ferry():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 90 #ferry starts facing East
    
    def move_forward(self, distance):
        if self.direction == 0:
            self.y += distance
        if self.direction == 90:
            self.x += distance
        if self.direction == 180:
            self.y -= distance
        if self.direction == 270:
            self.x -= distance
        
    def turn_left(self, degrees):
        self.direction -= degrees
        self.direction = self.direction % 360 #avoids the value of direction exceeding 360

    def turn_right(self, degrees):
        self.direction += degrees
        self.direction = self.direction % 360 #avoids the value of direction exceeding 360

    
    def strafe(self, movement_direction, distance):
        if movement_direction == 'E':
            self.x += distance
        if movement_direction == 'W':
            self.x -= distance
        if movement_direction == 'N':
            self.y += distance
        if movement_direction == 'S':
            self.y -= distance


#importing the input file and creating a list of tuples (k,v) with k = action and v = value

with open('input.txt', 'r') as f:
    a = f.read()

instruction_strings = a.splitlines()
instructions = []

for instruction_string in instruction_strings:
    k = instruction_string[0]
    v = int(instruction_string[1:])
    instructions.append((k,v))


u_boat = Ferry()

#running the instructions using the class methods defined above

for (action, value) in instructions:
    
    if action == 'F':
        u_boat.move_forward(value)
        continue
    if action == 'R':
        u_boat.turn_right(value)
        continue
    if action == 'L':
        u_boat.turn_left(value)
    if action in ['N', 'S', 'E', 'W']:
        u_boat.strafe(action, value)
        continue
    
#computing manhattan distance ie. sum of the absolute value of east-west position and nrth-south position
ew_position = abs(u_boat.x)
ns_position = abs(u_boat.y)

manhattan_distance = ew_position + ns_position
print(manhattan_distance)

