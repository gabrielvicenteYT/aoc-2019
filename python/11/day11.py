from array import array
from collections import defaultdict
from enum import Enum

with open('data.txt') as f:
    data = list(map(int, f.read().split(',')))


class Opcode(Enum):
    ADD = 1
    MUL = 2
    IN = 3
    OUT = 4
    JNZ = 5
    JZ = 6
    LT = 7
    EQ = 8
    REL = 9
    HALT = 99


class ParamMode(Enum):
    MEMORY = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Halt(Exception):
    pass


class Memory:
    def __init__(self, initial):
        self.data = array('q', initial)

    def __getitem__(self, index):
        return self.data[index] if index < len(self.data) else 0

    def __setitem__(self, index, value):
        if index >= len(self.data):
            self.data.extend([0] * (index - len(self.data)))
            self.data.append(value)
        else:
            self.data[index] = value


class Interpreter:
    def __init__(self, inp):
        self.pc = 0
        self.rel = 0
        self.memory = Memory(data)
        self.input = inp
        self.output = []

    def _param(self, index):
        mode = ParamMode(self.memory[self.pc] // 10 ** (index + 1) % 10)
        if mode == ParamMode.MEMORY:
            return self.memory[self.pc + index]
        if mode == ParamMode.IMMEDIATE:
            return self.pc + index
        if mode == ParamMode.RELATIVE:
            return self.rel + self.memory[self.pc + index]

    def param(self, index):
        return self.memory[self._param(index)]

    def store(self, index, value):
        self.memory[self._param(index)] = value

    def step(self):
        op = Opcode(self.memory[self.pc] % 100)
        if op == Opcode.ADD:
            self.store(3, self.param(1) + self.param(2))
            self.pc += 4
        elif op == Opcode.MUL:
            self.store(3, self.param(1) * self.param(2))
            self.pc += 4
        elif op == Opcode.IN:
            self.store(1, self.input())
            self.pc += 2
        elif op == Opcode.OUT:
            self.output.append(self.param(1))
            self.pc += 2
        elif op == Opcode.JNZ:
            self.pc = self.param(2) if self.param(1) else self.pc + 3
        elif op == Opcode.JZ:
            self.pc = self.pc + 3 if self.param(1) else self.param(2)
        elif op == Opcode.LT:
            self.store(3, self.param(1) < self.param(2))
            self.pc += 4
        elif op == Opcode.EQ:
            self.store(3, self.param(1) == self.param(2))
            self.pc += 4
        elif op == Opcode.REL:
            self.rel += self.param(1)
            self.pc += 2
        elif op == Opcode.HALT:
            raise Halt()

    def run_until_output(self):
        length = len(self.output)
        while len(self.output) == length:
            self.step()
        return self.output[-1]

    def run_until_halt(self):
        try:
            while 1:
                self.step()
        except Halt:
            return


def run(initial=()):
    result = defaultdict(int, initial)
    x = 0
    y = 0
    direction = 0
    interpreter = Interpreter(lambda: result[x, y])

    try:
        while True:
            result[x, y] = interpreter.run_until_output()
            direction += 1 if interpreter.run_until_output() else -1
            x += [0, 1, 0, -1][direction % 4]
            y += [-1, 0, 1, 0][direction % 4]
    except Halt:
        return result


print(len(run()))

part2 = run({(0, 0): 1})
min_x = min(x for x, _ in part2.keys())
max_x = max(x for x, _ in part2.keys())
min_y = min(y for _, y in part2.keys())
max_y = max(y for _, y in part2.keys())
for y in range(min_y, max_y + 1):
    print(*(' #'[part2[x, y]] for x in range(min_x, max_x + 1)))
