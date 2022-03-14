from dataclasses import dataclass


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __rep__(self):
        return f"({self.node_a} + {self.node_b})"
