from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float  # any

    def __to_str__(self):
        return f"{self.value}"
