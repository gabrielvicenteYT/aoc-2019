from enum import Enum


class Opcode(Enum):
    ADD = 1
    MUL = 2
    IN = 3
    OUT = 4
    JNZ = 5
    JZ = 6
    LT = 7
    EQ = 8
    EXIT = 99


class ParamMode(Enum):
    MEMORY = 0
    IMMEDIATE = 1


with open('data.txt') as f:
    data = list(map(int, f.read().split(',')))


def execute(inp):
    pc = 0
    memory = list(data)

    def param(index):
        mode = ParamMode(memory[pc] // 10 ** (index + 1) % 10)
        if mode == ParamMode.MEMORY:
            return memory[memory[pc + index]]
        elif mode == ParamMode.IMMEDIATE:
            return memory[pc + index]

    def store(index, value):
        memory[memory[pc + index]] = value

    inp = list(inp)
    out = []
    while True:
        op = Opcode(memory[pc] % 100)
        if op == Opcode.ADD:
            store(3, param(1) + param(2))
            pc += 4
        elif op == Opcode.MUL:
            store(3, param(1) * param(2))
            pc += 4
        elif op == Opcode.IN:
            store(1, inp.pop(0))
            pc += 2
        elif op == Opcode.OUT:
            out.append(param(1))
            pc += 2
        elif op == Opcode.JNZ:
            pc = param(2) if param(1) else pc + 3
        elif op == Opcode.JZ:
            pc = pc + 3 if param(1) else param(2)
        elif op == Opcode.LT:
            store(3, param(1) < param(2))
            pc += 4
        elif op == Opcode.EQ:
            store(3, param(1) == param(2))
            pc += 4
        elif op == Opcode.EXIT:
            return out


print(execute([1])[-1])
print(execute([5])[0])
