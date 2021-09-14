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

    def bracketCheck(self) -> dict:
        count = 0
        brackets = {}
        stack = []
        for i, e in enumerate(self.code):
            if e == "[":
                count += 1
                stack.append(i)
            elif e == "]":
                count -= 1
                if count < 0:
                    return {}

                brackets[stack.pop()] = i

        return brackets

    def execute(self):
        if not (brackets := self.bracketCheck()):
            raise SyntaxError("Bracket")

        offset = 0
        label = []
        skip = 0
        while offset < len(self.code):
            command = self.code[offset]
            if skip > 0:
                if command == "]":
                    skip -= 1

                offset += 1
                continue

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
                if self.addy[self.p] != 0:
                    label.append(offset - 1)
                else:
                    skip += 1
            elif command == "]":
                if self.addy[self.p] != 0:
                    offset = label.pop()

            offset += 1


if __name__ == '__main__':
    parser = BFParser("""++++++++++[>+++++++>++++++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.""")
    parser.execute()

    parser = BFParser("""+[,>[,.]<.>]""")
    parser.execute()
