class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

# Initialize spacecraft
initial_x = 0
initial_y = 0
initial_z = 0
initial_direction = "N"
spacecraft = Spacecraft(initial_x, initial_y, initial_z, initial_direction)

class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        elif self.direction == "Up":
            self.z += 1
        elif self.direction == "Down":
            self.z -= 1

    def move_backward(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "E":
            self.x -= 1
        elif self.direction == "W":
            self.x += 1
        elif self.direction == "Up":
            self.z -= 1
        elif self.direction == "Down":
            self.z += 1

    # ... (other methods)

# Rest of the code remains the same


class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == "N":
            self.y += 1
        # ... (other move methods)

    # ... (other methods)

def execute_commands(spacecraft, commands):
    for command in commands:
        if command == "f":
            spacecraft.move_forward()
        # ... (other command cases)

# Example commands
example_commands = ["f", "r", "u", "b", "l"]

# Initialize spacecraft
initial_x = 0
initial_y = 0
initial_z = 0
initial_direction = "N"
spacecraft = Spacecraft(initial_x, initial_y, initial_z, initial_direction)

# Execute commands
execute_commands(spacecraft, example_commands)

# Display final position and direction
print("Final Position:", (spacecraft.x, spacecraft.y, spacecraft.z))
print("Final Direction:", spacecraft.direction)
