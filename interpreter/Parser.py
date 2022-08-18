from nodes.AddNode import AddNode
from nodes.ExponentNode import ExponentNode
from nodes.PercentNode import PercentNode
from nodes.SubstractNode import SubstractNode
from nodes.ProductNode import ProductNode
from nodes.DivideNode import DivideNode
from dataclasses import dataclass
from nodes.PlusNode import PlusNode
from nodes.MinusNode import MinusNode
from nodes.NumberNode import NumberNode
from interpreter.Token import Token
from interpreter.TokenType import TokenType


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
        else:
            raise Exception("Unexpected token")
