""" Implemention of Doubly Linked List """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def prepend(self, data):
        new_node = Node(data)

        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

    def traverse_fw(self):
        current_node = self.__head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def traverse_bw(self):
        current_node = self.__tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev
