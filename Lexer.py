# DIGITS -> NUMBERS
# SYMBOL -> SYMBOLS

class Lexer:
    def __init__(self, text):
        self.text = text

    def move(self):
        self.current_char = self.text

    def gen_tokens(self):
        pass
