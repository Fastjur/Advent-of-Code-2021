f = open("input.txt", "r")
lines = f.readlines()

co2_lines = lines.copy()

i = -1
while len(lines) > 1:
    i = i + 1
    count = 0
    for j in range(len(lines)):
        count = count + (1 if lines[j][i] == '1' else -1)
    keep_char = '1' if count >= 0 else '0'
    lines = list(filter(lambda line: line[i] == keep_char, lines))

o2_binary = list(reversed(lines[0][0:]))
o2_binary.remove('\n')
result_o2 = 0
for (idx, i) in enumerate(o2_binary):
    result_o2 = result_o2 + 2 ** idx * int(i)

i = -1
while len(co2_lines) > 1:
    i = i + 1
    count = 0
    for j in range(len(co2_lines)):
        count = count + (1 if co2_lines[j][i] == '1' else -1)
    keep_char = '1' if count < 0 else '0'
    co2_lines = list(filter(lambda line: line[i] == keep_char, co2_lines))

result_co2 = 0
co2_binary = list(reversed(co2_lines[0][0:]))
co2_binary.remove('\n')
for (idx, i) in enumerate(co2_binary):
    result_co2 = result_co2 + 2 ** idx * int(i)

print("Oxygen:", result_o2)
print("CO2:", result_co2)
print("Result:", result_o2 * result_co2)
