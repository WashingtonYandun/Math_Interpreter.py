from dataclasses import dataclass


@dataclass
class MinusNode:
    node_a: any

    def __rep__(self):
        return f"(-{self.node_a})"
