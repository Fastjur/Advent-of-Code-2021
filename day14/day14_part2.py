from collections import defaultdict

lines = open("input.txt", "r").readlines()

polymer = lines[0].strip()
pairs = dict([l.strip().split(" -> ") for l in lines[2:]])

polymer_pairs = defaultdict(int)
for pair in pairs:
    polymer_pairs[pair] = 0

for i in range(len(polymer) - 1):
    pair = f"{polymer[i]}{polymer[i + 1]}"
    polymer_pairs[pair] += 1

letter_counts = defaultdict(int)
for c in polymer:
    letter_counts[c] += 1

print("Polymer", polymer)
print("Pair rules", pairs)
print("Pairs", polymer_pairs)
print("Letter counts", letter_counts)


steps = 40
for step in range(1, steps + 1):
    print(f"Step {step}")
    old_polymer_pairs = polymer_pairs.copy()
    for pair, amount in old_polymer_pairs.items():
        if amount > 0:
            inserted_char = pairs[pair]
            letter_counts[inserted_char] += amount
            pre_pair = f"{pair[0]}{inserted_char}"
            post_pair = f"{inserted_char}{pair[1]}"
            polymer_pairs[pre_pair] += amount
            polymer_pairs[post_pair] += amount
            polymer_pairs[pair] -= amount
    print(polymer_pairs)
    print(letter_counts)

max_counts = max(letter_counts.values())
min_counts = min(letter_counts.values())
print("Highest", max_counts)
print("Lowest", min_counts)
print("Answer", max_counts - min_counts)
