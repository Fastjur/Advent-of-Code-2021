f = open("input.txt", "r")
lines = f.readlines()

lines = [int(i) for i in lines if i != ""]

prev_value = lines[0]
count_larger = 0
for line in lines[1:]:
    if line > prev_value:
        count_larger = count_larger + 1
    prev_value = line

print(count_larger)