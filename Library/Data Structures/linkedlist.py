# Class for a doubly linked list

class LinkedListNode:
    def __init__(self, data=None, previous=None, nextNode=None):
        self.data = data
        self.previousNode = previous
        self.nextNode = nextNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nextNode
