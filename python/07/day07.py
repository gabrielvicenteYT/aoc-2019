from enum import Enum
from itertools import permutations, cycle

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
    HALT = 99


class ParamMode(Enum):
    MEMORY = 0
    IMMEDIATE = 1


class Halt(Exception):
    pass


class Interpreter:
    def __init__(self, inp):
        self.pc = 0
        self.memory = list(data)
        self.input = inp
        self.output = []

    def param(self, index):
        mode = ParamMode(self.memory[self.pc] // 10 ** (index + 1) % 10)
        if mode == ParamMode.MEMORY:
            return self.memory[self.memory[self.pc + index]]
        elif mode == ParamMode.IMMEDIATE:
            return self.memory[self.pc + index]

    def store(self, index, value):
        self.memory[self.memory[self.pc + index]] = value

    def step(self):
        op = Opcode(self.memory[self.pc] % 100)
        if op == Opcode.ADD:
            self.store(3, self.param(1) + self.param(2))
            self.pc += 4
        elif op == Opcode.MUL:
            self.store(3, self.param(1) * self.param(2))
            self.pc += 4
        elif op == Opcode.IN:
            self.store(1, self.input.pop(0))
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
        elif op == Opcode.HALT:
            raise Halt()

    def run_until_output(self):
        length = len(self.output)
        while len(self.output) == length:
            self.step()
        return self.output[-1]


part1 = -1
for phases in permutations(range(5), 5):
    thrust = 0
    for phase in phases:
        interpreter = Interpreter([phase, thrust])
        thrust = interpreter.run_until_output()
    part1 = max(thrust, part1)
print(part1)

part2 = -1
for phases in permutations(range(5, 10), 5):
    interpreters = [Interpreter([phase]) for phase in phases]
    thrust = 0
    try:
        for interpreter in cycle(interpreters):
            interpreter.input.append(thrust)
            thrust = interpreter.run_until_output()
    except Halt:
        part2 = max(interpreters[-1].output[-1], part2)
print(part2)
