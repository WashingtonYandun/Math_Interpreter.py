from Lexer import Lexer


while True:
    text = input("(W$)> ")
    lexer = Lexer(text)
    tokens = lexer.gen_tokens()
    print(list(tokens))
