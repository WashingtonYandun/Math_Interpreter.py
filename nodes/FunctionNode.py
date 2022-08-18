from dataclasses import dataclass


@dataclass
class FunctionNode:
    node_func: any
    node_lp: any
    node_rp: any
    node_num: any

    def __to_str__(self):
        return f"({self.node_func} {self.node_lp} {self.node_num} {self.node_rp})"
