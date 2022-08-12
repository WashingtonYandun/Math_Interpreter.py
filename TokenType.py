from dataclasses import dataclass
from enum import Enum
from lib2to3.pgen2.token import PERCENT


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
    PERCENT = iota()
    EXPONENT = iota()

    L_PAR = iota()
    R_PAR = iota()
    L_BRAC = iota()
    R_BRAC = iota()
    L_CURL = iota()
    R_CURL = iota()

    FUNCTION = iota()
