#!/usr/bin/python3
"""
This module defines a Node and SinglyLinkedList classes.

The Node class defines a node of a singly linked list.
The SinglyLinkedList class defines a singly linked list.

The Node class includes a method to set and retrieve the data stored,
and a method to set and retrieve the next node in the linked list.

The SinglyLinkedList class includes a method to insert a new Node into
the correct sorted position in the list, and a method to print the
entire list in stdout, one node number by line.
"""


class Node:
    """Defines a node of a singly linked list.

    Attributes:
        __data (int): data stored inside the node.
        __next_node (Node): next node in the linked list.

    """

    def __init__(self, data, next_node=None):
        """Initializes a Node.

        Args:
            data (int): data to be stored in the node.
            next_node (Node, optional): next node.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node.

        Returns:
            The data of the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): data to be stored in the node.

        Raises:
            TypeError: If data is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Gets the next node.

        Returns:
            The next node.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node.

        Args:
            value (Node): next node in the linked list.

        Raises:
            TypeError: If next_node is not a Node object or None.

        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list.

    Attributes:
        __head (Node): head of the linked list.

    """

    def __init__(self):
        """Initializes a SinglyLinkedList.

        """
        self.__head = None

    def __str__(self):
        """Returns a string representation of the linked list.

        Returns:
            A string representation of the linked list.

        """
        nodes = []
        node = self.__head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): data to be stored in the new node.

        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
