from dataclasses import dataclass


@dataclass
class SubstractNode:
    node_a: any
    node_b: any

    def __to_str__(self):
        return f"({self.node_a} - {self.node_b})"
