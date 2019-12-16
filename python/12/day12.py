import math
import re
from functools import reduce
from itertools import count

with open('data.txt') as f:
    data = [[*map(int, re.findall(r'-?\d+', line))] for line in f]

positions = [*map(list, data)]
velocities = [[0] * 3 for _ in range(len(positions))]
for _ in range(1000):
    for i in range(len(positions)):
        for j in range(len(positions)):
            for c in range(3):
                if positions[i][c] < positions[j][c]:
                    velocities[i][c] += 1
                elif positions[i][c] > positions[j][c]:
                    velocities[i][c] -= 1
    for i in range(len(positions)):
        for c in range(3):
            positions[i][c] += velocities[i][c]

print(sum(
    sum(map(abs, position)) * sum(map(abs, velocity))
    for position, velocity in zip(positions, velocities)
))

cycle_lengths = []

for c in range(3):
    positions = [d[c] for d in data]
    initial_positions = positions[:]
    velocities = [0] * len(data)
    initial_velocities = velocities[:]
    for steps in count():
        for i in range(len(data)):
            for j in range(len(data)):
                if positions[i] < positions[j]:
                    velocities[i] += 1
                elif positions[i] > positions[j]:
                    velocities[i] -= 1
        for i in range(len(data)):
            positions[i] += velocities[i]
        if positions == initial_positions and velocities == initial_velocities:
            cycle_lengths.append(steps + 1)
            break

print(reduce(lambda a, b: a * b // math.gcd(a, b), cycle_lengths))
