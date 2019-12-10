from math import gcd, atan2

with open('data.txt') as f:
    data = f.read().split('\n')

width = len(data[0])
height = len(data)


def asteroid_locations():
    for y in range(height):
        for x in range(width):
            if data[y][x] == '#':
                yield x, y


def visible(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        return False
    g = gcd(dx, dy)
    dx //= g
    dy //= g
    x1 += dx
    y1 += dy
    while x1 != x2 or y1 != y2:
        if data[y1][x1] == '#':
            return False
        x1 += dx
        y1 += dy
    return True


def main():
    part1, station_x, station_y = max(
        (sum(visible(x1, y1, x2, y2) for x2, y2 in asteroid_locations()), x1, y1)
        for x1, y1 in asteroid_locations()
    )
    print(part1)

    def angle_from_station(xy):
        x, y = xy
        return -atan2(x - station_x, y - station_y)

    sorted_asteroids = sorted(
        ((x, y) for x, y in asteroid_locations() if not (x == station_x and y == station_y)),
        key=angle_from_station
    )

    for _ in range(200):
        part2 = next((x, y) for x, y in sorted_asteroids if visible(station_x, station_y, x, y))
        sorted_asteroids.remove(part2)
    print('%d%02d' % part2)


if __name__ == '__main__':
    main()
