x = 0
y = 0

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

direction = NORTH

file = open("input.txt")
file = file.readlines()
for line in file:
    commands = line.split(", ")
    for command in commands:
        mod = 0
        print(command)
        dir = command[0]
        if dir == "R":
            mod = 1
        else:
            mod = -1
        direction += mod
        direction %= 4
        distance = int(command[1:])
        if direction == NORTH:
            y += distance
        elif direction == EAST:
            x += distance
        elif direction == SOUTH:
            y -= distance
        elif direction == WEST:
            x -= distance

print(x, y)
