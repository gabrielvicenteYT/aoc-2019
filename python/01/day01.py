with open('data.txt') as f:
    data = [*map(int, f)]

print(sum(int(x) // 3 - 2 for x in data))


def cost(n):
    result = 0
    while n >= 9:
        n = n // 3 - 2
        result += n
    return result


print(sum(map(cost, data)))
