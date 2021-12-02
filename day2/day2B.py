f = open("input.txt", "r")
lines = f.readlines()

depth = 0
horizontal_pos = 0
aim = 0

for line in lines:
    cmd = line.split()
    if cmd[0] == "down":
        aim = aim + int(cmd[1])
    if cmd[0] == "up":
        aim = aim - int(cmd[1])
    if cmd[0] == "forward":
        horizontal_pos = horizontal_pos + int(cmd[1])
        depth = depth + aim * int(cmd[1])
    if cmd[0] == "backward":
        horizontal_pos = horizontal_pos - int(cmd[1])

print(f"depth: {depth}, horizontal_pos: {horizontal_pos}")
print(f"depth * horizontal_pos: {depth * horizontal_pos}")