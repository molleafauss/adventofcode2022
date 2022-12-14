import math

from advent import Solver
import re

# https://adventofcode.com/2022/day/11
# ok I had no clue about how to reduce the math - the use modulo of all "divisible by" was a hint that lead to the right
# solution
RE_MONKEY = re.compile(r"Monkey (\d+):")
RE_ITEMS = re.compile("Starting items: (.*)")
RE_OPERATION = re.compile("Operation: new = (.*)")
RE_TEST = re.compile(r"Test: divisible by (\d*)")
RE_RESULT_FALSE = re.compile(r"If false: throw to monkey (\d*)")
RE_RESULT_TRUE = re.compile(r"If true: throw to monkey (\d*)")


class Monkey:
    def __init__(self, id):
        self.id = int(id)
        self.initial_items = []
        self.items = None
        self.inspected = 0
        self.operation = None
        # divisor, true, false
        self.test = [None, None, None]

    def set_items(self, text):
        self.initial_items += [int(x.strip()) for x in text.split(",")]

    def set_operation(self, text):
        # need parsing
        self.operation = text

    def set_test(self, value):
        self.test[0] = int(value)

    def set_test_result(self, result, monkey):
        self.test[1 if result else 2] = int(monkey)

    def add_item(self, item):
        self.items.append(item)

    def start(self):
        self.items = self.initial_items.copy()
        self.inspected = 0

    def act(self, reduce_worry, reducer):
        throws = []
        while self.items:
            self.inspected += 1
            worry = self.items.pop(0)
            # this is "cheating", but, well, it works.
            worry = eval(self.operation, {}, {"old": worry}) % reducer
            worry = int(worry / reduce_worry)
            if (worry % self.test[0]) == 0:
                throws.append([self.test[1], worry])
            else:
                throws.append([self.test[2], worry])
        return throws


class Solution(Solver):
    def __init__(self):
        self.monkeys = []

    def parse(self, line: str):
        if mo := RE_MONKEY.match(line):
            self.monkeys.append(Monkey(mo.group(1)))
        elif mo := RE_ITEMS.search(line):
            self.monkeys[-1].set_items(mo.group(1))
        elif mo := RE_OPERATION.search(line):
            self.monkeys[-1].set_operation(mo.group(1))
        elif mo := RE_TEST.search(line):
            self.monkeys[-1].set_test(mo.group(1))
        elif mo := RE_RESULT_TRUE.search(line):
            self.monkeys[-1].set_test_result(True, mo.group(1))
        elif mo := RE_RESULT_FALSE.search(line):
            self.monkeys[-1].set_test_result(False, mo.group(1))
        elif line.strip() == "":
            pass
        else:
            raise ValueError(f"Invalid line: {line}")

    def solve(self):
        reducer = math.prod([m.test[0] for m in self.monkeys])
        print(f"reducer: {reducer}")
        for m in self.monkeys:
            m.start()
        for i in range(20):
            for m in self.monkeys:
                for (id, item) in m.act(3, reducer):
                    self.monkeys[id].add_item(item)

        # sort by most inspected, take first twos
        most_active = sorted(self.monkeys, reverse=True, key=lambda m: m.inspected)
        print(f"[1] Most active: {most_active[0].id} => {most_active[0].inspected}, {most_active[1].id} => {most_active[1].inspected}: {most_active[0].inspected * most_active[1].inspected}")

        # reset
        for m in self.monkeys:
            m.start()
        for i in range(10000):
            for m in self.monkeys:
                for (id, item) in m.act(1, reducer):
                    self.monkeys[id].add_item(item)
            if i % 1000 == 0:
                print("[%s] %s" % (i, [m.inspected for m in self.monkeys]))

        # sort by most inspected, take first twos
        most_active = sorted(self.monkeys, reverse=True, key=lambda m: m.inspected)
        print(f"[1] Most active: {most_active[0].id} => {most_active[0].inspected}, {most_active[1].id} => {most_active[1].inspected}: {most_active[0].inspected * most_active[1].inspected}")

    def file_name(self):
        return "../files/day11-monkeys.txt"

    def test_data(self):
        return """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
