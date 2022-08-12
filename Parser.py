from AddNode import AddNode
from ExponentNode import ExponentNode
from PercentNode import PercentNode
from SubstractNode import SubstractNode
from ProductNode import ProductNode
from DivideNode import DivideNode
from dataclasses import dataclass
from PlusNode import PlusNode
from MinusNode import MinusNode
from NumberNode import NumberNode
from Token import Token
from TokenType import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.move()

    def move(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None

        res = self.parse_expr()

        if self.current_token != None:
            raise Exception("Unexpected token")

        return res

    def parse_expr(self):
        res = self.parse_term()

        while self.current_token != None and self.current_token.type in [TokenType.PLUS, TokenType.MINUS]:
            if self.current_token.type == TokenType.PLUS:
                self.move()
                res = AddNode(res, self.parse_term())
            elif self.current_token.type == TokenType.MINUS:
                self.move()
                res = SubstractNode(res, self.parse_term())

        return res

    def parse_term(self):
        res = self.parse_factor()

        while self.current_token != None and self.current_token.type in [TokenType.PRODUCT, TokenType.DIVIDE, TokenType.EXPONENT, TokenType.PERCENT]:
            if self.current_token.type == TokenType.PRODUCT:
                self.move()
                res = ProductNode(res, self.parse_factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.move()
                res = DivideNode(res, self.parse_factor())
            elif self.current_token.type == TokenType.EXPONENT:
                self.move()
                res = ExponentNode(res, self.parse_factor())
            elif self.current_token.type == TokenType.PERCENT:
                self.move()
                res = PercentNode(res, self.parse_factor())

        return res

    def parse_factor(self):
        current_token = self.current_token
        if current_token.type == TokenType.NUMBER:
            self.move()
            return NumberNode(current_token.value)
            '''
            elif self.current_token.type == TokenType.L_PAR:
            self.move()
            res = self.parse_factor()
            if current_token.type != TokenType.R_PAR:
                raise Exception("Expected )")
            self.move()
            return res
            
            elif current_token.type == TokenType.FUNCTION:
                self.move()
                if current_token.type != TokenType.L_PAR:
                    raise Exception("Expected (")
                self.move()
                res = self.parse_expr()
                if current_token.type != TokenType.R_PAR:
                    raise Exception("Expected )")
                self.move()
                return res
            '''
        else:
            raise Exception("Unexpected token")
