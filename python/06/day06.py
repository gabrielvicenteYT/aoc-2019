with open('data.txt') as f:
    data = [line.rstrip().split(')') for line in f]

parent_map = {child: parent for parent, child in data}


def parents(obj):
    while obj in parent_map:
        obj = parent_map[obj]
        yield obj


def ilen(iterable):
    return sum(1 for _ in iterable)


print(sum(ilen(parents(obj)) for obj in parent_map.keys()))

santa_parents = list(parents('SAN'))

for i, obj in enumerate(parents('YOU')):
    try:
        j = santa_parents.index(obj)
        print(i + j)
        break
    except ValueError:
        pass
