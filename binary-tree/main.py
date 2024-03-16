import random

from tree import Node


def main():
    root = Node(0.5)
    [root.insert(random.random()) for _ in range(100)]
    root.print()


if __name__ == "__main__":
    main()
