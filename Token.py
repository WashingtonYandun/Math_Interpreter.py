from dataclasses import dataclass
from TokenType import TokenType


@dataclass
class Token:
    type: TokenType
    value: any = None  # depends on the token type

    def __rep__(self):
        return self.type.name + f"{self.value}" if self.value != None else ""
