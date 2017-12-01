x = 0
y = 0

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

direction = NORTH

file = open("input.txt")
file = file.readlines()

hasBeen = []

for line in file:
    commands = line.split(", ")
    for command in commands:
        mod = 0
        dir = command[0]
        if dir == "R":
            mod = 1
        else:
            mod = -1
        direction += mod
        direction %= 4
        distance = int(command[1:])
        prevX = x
        prevY = y
        if direction == NORTH:
            y += distance
        elif direction == EAST:
            x += distance
        elif direction == SOUTH:
            y -= distance
        elif direction == WEST:
            x -= distance
        
        def insert(a,b):
            if (a,b) in hasBeen:
                print(a,b)
            else:
                hasBeen.append((a,b))

        if x != prevX:
            for i in range(1, abs(x - prevX)):
                if x - prevX > 0:
                    insert(prevX + i,y)
                else:
                    insert(prevX - i,y)
        if y != prevY:
            for i in range(1, abs(y - prevY)):
                if y - prevY > 0:
                    insert(x,prevY + i)
                else:
                    insert(x,prevY - i)


print(abs(x) + abs(y))
