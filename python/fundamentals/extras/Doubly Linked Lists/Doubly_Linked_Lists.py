class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_node(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                break
            current = current.next

    def insert_node_before(self, existing_val, new_val):
        new_node = Node(new_val)
        current = self.head
        while current is not None:
            if current.value == existing_val:
                if current.prev is not None:
                    current.prev.next = new_node
                    new_node.prev = current.prev
                new_node.next = current
                current.prev = new_node
                if current == self.head:
                    self.head = new_node
                break
            current = current.next

    def print_values(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        print(" -> ".join(map(str, values)))

# Test the DoublyLinkedList class
my_list = DoublyLinkedList()
my_list.add_to_end(1)
my_list.add_to_end(2)
my_list.add_to_end(3)
my_list.print_values()
my_list.delete_node(2)
my_list.insert_node_before(3, 4)
my_list.print_values()