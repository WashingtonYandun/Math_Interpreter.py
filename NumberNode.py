from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float  # any

    def __rep__(self):
        return f"{self.value}"
