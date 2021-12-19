import numpy as np

lines = open("input.txt", "r").readlines()

polymer = lines[0].strip()
pairs = [l.strip().split(" -> ") for l in lines[2:]]
pairs = dict(map(lambda pair: [pair[0], f"{pair[0][0]}{pair[1]}"], pairs))

print(polymer)

steps = 10
for step in range(1, steps + 1):
    insertions = 0
    new_polymer = ""
    last_char = ""
    print("Step", step)
    for (idx, _) in enumerate(polymer):
        if idx == len(polymer) - 1:
            new_polymer += last_char
            break
        pair = f"{polymer[idx]}{polymer[idx + 1]}"
        replacement = pairs[pair]
        if len(replacement) > 0:
            new_polymer += replacement
            last_char = pair[1]
    polymer = new_polymer
    # print(new_polymer)

# print("Final polymer")
# print(polymer)

polymer_array = [c for c in polymer]
unique, counts = np.unique(polymer_array, return_counts= True)
print("Occurences", dict(zip(unique, counts)))