from collections import Counter

puzzle_input = 171309, 643603

part1 = 0
part2 = 0
for password in map(str, range(*puzzle_input)):
    if all(password[i] <= password[i + 1] for i in range(len(password) - 1)):
        counts = Counter(password)
        if any(value >= 2 for value in counts.values()):
            part1 += 1
        if 2 in counts.values():
            part2 += 1

print(part1)
print(part2)
