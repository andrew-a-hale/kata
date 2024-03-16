from __future__ import annotations

import abc
import json
from typing import Dict, List, Tuple


class TreeNode:
    def __init__(self: TreeNode, data: Dict):
        self._data = data
        self._children = []
        self._parent = []

    def get_id(self: TreeNode) -> int:
        return int(self._data.get("id"))

    def add_child(self: TreeNode, child: TreeNode) -> None:
        self._children.append(child)

    def get_children(self: TreeNode) -> List[int]:
        return [child.get_id() for child in self._children]

    def get_parents(self: TreeNode) -> List[int]:
        return [parent.get_id() for parent in self._parent]

    def add_parent(self: TreeNode, parent: TreeNode) -> None:
        self._parent.append(parent)

    def get_related_parents(self: TreeNode):
        parents = set([parent for child in self._children for parent in child._parent])
        return parents

    def __lt__(self: TreeNode, other: TreeNode) -> bool:
        return self.get_id() < other.get_id()

    def __str__(self: TreeNode) -> str:
        return json.dumps(
            {
                "id": self.get_id(),
                "parent": self.get_parents(),
                "children": self.get_children(),
            }
        )


class AbstractNode(abc.ABC):
    def __init__(self):
        pass

    def add_edge(self, node):
        pass

    def get_neighbours(self):
        pass

    def __str__(self):
        pass


class Node(AbstractNode):
    def __init__(
        self: AbstractNode, data: dict = None, edges: List[AbstractNode] = None
    ):
        self._data = data
        self._edges = edges

    def add_edge(self, node: AbstractNode) -> None:
        self._edges.append(node)

    def get_neighbours(self) -> List[AbstractNode]:
        return self._edges

    def __str__(self) -> None:
        node_string = f"Node {self._data.get('id')}: "
        node_string += json.dumps(self._data)
        if self._edges:
            node_string += f"\nNode {self._data.get('id')} Edges:\n"
            node_string += ", ".join([n.__str__() for n in self._edges])
        return node_string


class BTree:
    def __init__(self, **kwargs):
        self._data = kwargs
        self._left = None
        self._right = None

    def insert(self, node):
        if node._data["id"] > self._data["id"] and self._right:
            self._right.insert(node)
        elif node._data["id"] > self._data["id"]:
            self._right = node
        elif node._data["id"] <= self._data["id"] and self._left:
            self._left.insert(node)
        else:
            self._left = node

    def print(self):
        if self._left:
            self._left.print()
        print(self._data["id"])
        if self._right:
            self._right.print()
