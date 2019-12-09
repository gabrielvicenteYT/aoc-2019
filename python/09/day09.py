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


class Interpreter:
    def __init__(self, inp):
        self.pc = 0
        self.rel = 0
        self.memory = defaultdict(int, enumerate(data))
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


interpreter = Interpreter([1])
interpreter.run_until_halt()
print(interpreter.output)

interpreter = Interpreter([2])
interpreter.run_until_halt()
print(interpreter.output)
