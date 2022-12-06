from typing import Protocol


# Parser "interface" used by the loader
class Parser(Protocol):
    def parse(self, line: str):
        ...

    def solve(self):
        ...

    def file_name(self):
        return ""

    def test_data(self):
        return ""

    def run_test(self):
        for l in self.test_data().split("\n"):
            self.parse(l.rstrip())
        self.solve()

    def run(self):
        with open(self.file_name()) as f:
            for l in f:
                self.parse(l.rstrip())
        self.solve()


# reads a file line by line, passes each line to the parser and then call solve on the parser
def loader(filename: str, parser: Parser):
    with open(filename) as f:
        for l in f:
            parser.parse(l.rstrip())
    parser.solve()
