from interpreter.Lexer import Lexer
from interpreter.Parser import Parser

while True:
    text = input("(W$) > ")
    lexer = Lexer(text)
    tokens = lexer.gen_tokens()
    parser = Parser(tokens)
    exp_tree = parser.parse()
    print(exp_tree)
