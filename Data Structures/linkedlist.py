# Content originally learned at GeeksForGeeks
# Class for a doubly linked list

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.previousNode = None
        self.nextNode = None


class doublyLinkedList:
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

    def print_linked_list_reverse(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n.nextNode is not None:
                n = n.nextNode
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.previousNode
