from dataclasses import dataclass
from TokenType import TokenType


@dataclass
class Token:
    type: TokenType
    value: any = None  # depends on the token type

    def __to_str__(self):
        if self.type == TokenType.NUMBER:
            return f"{self.type.name} : {int(self.value)}"
        elif self.type == TokenType.FUNCTION:
            return f"{self.type.name} : {self.value}"
        else:
            return f"{self.type.name}"
