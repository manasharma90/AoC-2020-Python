class Car():
    def __init__(self, color, model):
        self.x = 0
        self.y = 0
        self.direction = 90
        self.color = color
        self.model = model

    def turn_right(self):
        self.direction += 90

    def turn_left(self):
        self.direction -=90

    def move_forward(self, distance):
        if self.direction == 90:
            self.x += distance
    
    def move_backward(self, distance):
        pass

    def strafe(self, movement_direction, distance):
        if movement_direction == "east":
            self.x += distance


v = Car("Silver", "Veanu")

print(v.model)

v.turn_left()
v.turn_right()
print(v.direction)
