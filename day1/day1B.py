f = open("input.txt", "r")
lines = f.readlines()

lines = [int(i) for i in lines if i != ""]

prev_value = lines[0] + lines[1] + lines[2]
count_larger = 0
for i in range(3, len(lines)):
    value = lines[i-2] + lines[i-1] + lines[i]
    if value > prev_value:
        count_larger = count_larger + 1
    prev_value = value

print(count_larger)