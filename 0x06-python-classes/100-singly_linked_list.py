#!/usr/bin/python3

"""Define node for a singly-linked list."""

class Node:
    """classe node"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node."""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeErrorr("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
