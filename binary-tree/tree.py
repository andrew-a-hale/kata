from __future__ import annotations


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value:
            if value <= self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

    def print(self):
        if self.left:
            self.left.print()
        print(self.value)
        if self.right:
            self.right.print()
