class EightBit(int):
    def __init__(self, n: int):
        self.n = n & 0xFF

    def __add__(self, other: int):
        return (self.n + other) & 0xFF

    def __sub__(self, other: int):
        return (self.n - other) & 0xFF


class BFParser:
    def __init__(self, code: str) -> None:
        self.code = code
        self.p = EightBit(0)
        self.addy = [0] * 29999

    def bracketCheck(self) -> bool:
        brackets = 0
        for i in self.code:
            if i == "[":
                brackets += 1
            elif i == "]":
                brackets -= 1

        return brackets == 0

    def execute(self):
        if not self.bracketCheck():
            raise SyntaxError("Bracket")

        offset = 0
        label = 0
        while offset < len(self.code):
            command = self.code[offset]

            if command == ">":
                self.p += 1
            elif command == "<":
                self.p -= 1
            elif command == "+":
                self.addy[self.p] += 1
            elif command == "-":
                self.addy[self.p] -= 1
            elif command == ".":
                print(chr(self.addy[self.p]), end="")
            elif command == ",":
                inp = input()
                if len(inp) > 0:
                    inp = inp[0]
                    if ord(inp) < 128:
                        self.addy[self.p] = ord(inp)
            elif command == "[":
                label = offset
            elif command == "]":
                if self.addy[self.p] != 0:
                    offset = label

            offset += 1


if __name__ == '__main__':
    parser = BFParser("""++++++++++[>+++++++>++++++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.""")
    parser.execute()
