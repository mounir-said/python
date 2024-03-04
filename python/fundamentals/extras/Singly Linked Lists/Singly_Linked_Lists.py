class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node

    def print_values(self):
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next

    def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()