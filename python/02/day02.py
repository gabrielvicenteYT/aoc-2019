with open('data.txt') as f:
    data = [*map(int, f.read().split(','))]


def execute(noun, verb):
    pc = 0
    memory = [*data]
    memory[1] = noun
    memory[2] = verb
    while True:
        op, in1, in2, out = memory[pc:pc + 4]
        if op == 1:
            memory[out] = memory[in1] + memory[in2]
        elif op == 2:
            memory[out] = memory[in1] * memory[in2]
        elif op == 99:
            return memory[0]
        pc += 4


print(execute(12, 2))
print(next(
    '%02d%02d' % (noun, verb)
    for noun in range(100)
    for verb in range(100)
    if execute(noun, verb) == 19690720
))
