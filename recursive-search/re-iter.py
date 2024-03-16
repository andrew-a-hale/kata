import itertools
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Prefix:
    layers: field(default_factory=list)

    def add_layers(self, layers: list[list[str]]) -> None:
        for layer in layers:
            self.layers.append(layer)

    def compute_paths(self, strategy: Callable) -> list[str]:
        if len(self.layers) == 0:
            return []
        return strategy(*self.layers)


def fun_search(*layers: list[str]) -> list[str]:
    return ["".join("/" + y for y in x) for x in itertools.product(*layers)]


def rec_search(*layers: list[str]) -> list[str]:
    item_list = []

    def _search(layer, rest, item):
        for part in layer:
            if len(rest) == 0:
                item_list.append(item + f"/{part}")
            else:
                _search(rest[0], rest[1:], item + f"/{part}")

    _search(layers[0], layers[1:], "")

    return item_list


prefix = Prefix([])
l0 = ["root", "a"]
l1 = ["m", "n", "o"]
l2 = ["w", "x", "y"]
l3 = ["z", "0"]

prefix.add_layers([l0, l1, l2, l3])
f = prefix.compute_paths(fun_search)
r = prefix.compute_paths(rec_search)
