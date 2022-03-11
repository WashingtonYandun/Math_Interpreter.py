from dataclasses import dataclass
from enum import Enum

iota_count = 0


def iota(restart=False):
    global iota_count
    if restart:
        iota_count = 0
    c = iota_count
    iota_count = iota_count + 1
    return c


class TokenType(Enum):
    NUMBER = iota()
    PLUS = iota()
    MINUS = iota()
    PRODUCT = iota()
    DIVIDE = iota()
    L_PAR = iota()
    R_PAR = iota()


@dataclass
class Token:
    type: TokenType
    value: any = None  # depends on the token type

    def __dev__(self):
        val = f":{self.value}" if self.value != None else ""
        return self.type.name + val
