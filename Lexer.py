# DIGITS -> NUMBERS
# SYMBOL -> SYMBOLS

from Token import Token, TokenType


class Lexer:
    def __init__(self, text):
        self.text = iter(text)  # for using next function
        self.move()

    def move(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def gen_number(self):
        decimal_counter = 0  # for controlling the correct number of decimal points
        num_str = self.current_char
        self.move()

        while self.current_char != None and (self.current_char == '.' or self.current_char in '0123456789'):
            if decimal_counter > 1:
                # if there is more than one decimal point - break (cause error)
                raise Exception(f"Illegal char '{self.current_char}'")

            if self.current_char == '.':
                decimal_counter += 1
            num_str = num_str + self.current_char
            self.move()

        if num_str.startswith("."):
            num_str = "0" + num_str

        if num_str.endswith("."):
            num_str = num_str + "0"

        return Token(TokenType.NUMBER, float(num_str))

    def gen_tokens(self):
        while self.current_char != None:
            if self.current_char in ' \n\t':
                # ignore the whitespaces
                self.move()
            elif self.current_char == '.' or self.current_char in '0123456789':
                # use yield for 'returning' multiple stuff (tokens)
                yield self.gen_number()
            elif self.current_char == "+":
                yield Token(TokenType.PLUS)
                self.move()
            elif self.current_char == "-":
                yield Token(TokenType.MINUS)
                self.move()
            elif self.current_char == "*":
                yield Token(TokenType.PRODUCT)
                self.move()
            elif self.current_char == "/":
                yield Token(TokenType.DIVIDE)
                self.move()
            elif self.current_char == "(":
                yield Token(TokenType.L_PAR)
                self.move()
            elif self.current_char == ")":
                yield Token(TokenType.R_PAR)
                self.move()
            else:
                # throw error
                raise Exception(f"Illegal char '{self.current_char}' ")
