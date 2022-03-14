from dataclasses import dataclass


@dataclass
class PlusNode:
    node_a: any

    def __rep__(self):
        return f"(+{self.node_a})"
