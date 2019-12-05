with open('data.txt') as f:
    data1, data2, *_ = f

wire1 = data1.rstrip().split(',')
wire2 = data2.rstrip().split(',')

grid1 = {}
grid2 = {}

for i, wire in ((grid1, wire1), (grid2, wire2)):
    x = y = 0
    dist = 0
    for section in wire:
        direction = section[0]
        if direction == 'U':
            dx, dy = 0, 1
        elif direction == 'D':
            dx, dy = 0, -1
        elif direction == 'L':
            dx, dy = 1, 0
        elif direction == 'R':
            dx, dy = -1, 0
        else:
            raise ValueError(f'Unknown direction {direction}')
        length = int(section[1:])
        for _ in range(length):
            x += dx
            y += dy
            dist += 1
            i[x, y] = dist

common_keys = set(grid1.keys()) & set(grid2.keys())
print(min(abs(a) + abs(b) for a, b in common_keys))
print(min(grid1[k] + grid2[k] for k in common_keys))
