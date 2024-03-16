import random

from node import BTree

tree = BTree(id=10)
[tree.insert(BTree(id=random.randint(0, 20))) for _ in range(10)]
tree.print()
