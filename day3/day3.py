f = open("input.txt", "r")
lines = f.readlines()

gammaBinary = [0] * (len(lines[0]) - 1)

for line in lines:
    for (idx, char) in enumerate(line):
        if char != '\n':
            gammaBinary[idx] = gammaBinary[idx] + (1 if char == '1' else -1)


for i in range(len(gammaBinary)):
    gammaBinary[i] = 1 if gammaBinary[i] > 0 else 0

gamma = 0
epsilon = 0
for (idx, i) in enumerate(reversed(gammaBinary)):
    gamma = gamma + 2**idx * int(i)
    epsilon = epsilon + 2**idx * (1 - int(i))

print("Result:", gamma * epsilon)