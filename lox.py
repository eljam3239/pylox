import sys

class Lox:
    had_error = False

    @staticmethod
    def main(args):
        if len(args) > 1:
            print("Usage: pylox [script]")
            sys.exit(64)
        elif len(args) == 1:
            Lox.run_file(args[0])
        else:
            Lox.run_prompt()

    @staticmethod
    def run_file(path):
        with open(path, 'r') as file:
            Lox.run(file.read())
        # Indicate an error in the exit code.
        if Lox.had_error:
            sys.exit(65)

    @staticmethod
    def run_prompt():
        while True:
            try:
                line = input("> ")
                if line.strip() == "":
                    break
                Lox.run(line)
                Lox.had_error = False
            except EOFError:
                break

    @staticmethod
    def run(source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        # For now, just print the tokens.
        for token in tokens:
            print(token)

    @staticmethod
    def error(line, message):
        Lox.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}")
        Lox.had_error = True

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []

    def scan_tokens(self):
        # This is a stub for the actual scanning logic.
        # In a full implementation, this method would tokenize the input source code.
        return self.tokens

class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"{self.type} {self.lexeme} {self.literal}"

if __name__ == "__main__":
    Lox.main(sys.argv)