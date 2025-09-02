class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_back(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return self

    def print_forward(self):
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next
        return self

    def print_backward(self):
        runner = self.tail
        while runner is not None:
            print(runner.value)
            runner = runner.prev
        return self

    def delete(self, val):
        runner = self.head
        while runner is not None:
            if runner.value == val:
                if runner.prev is None:  # head node
                    self.head = runner.next
                    if self.head:
                        self.head.prev = None
                elif runner.next is None:  # tail node
                    self.tail = runner.prev
                    if self.tail:
                        self.tail.next = None
                else:  # middle node
                    runner.prev.next = runner.next
                    runner.next.prev = runner.prev
                return self
            runner = runner.next
        return self

    def insert_before(self, val, before_val):
        runner = self.head
        while runner is not None:
            if runner.value == before_val:
                new_node = Node(val)
                new_node.next = runner
                new_node.prev = runner.prev

                if runner.prev is None:
                    self.head = new_node
                else:
                    runner.prev.next = new_node

                runner.prev = new_node
                return self
            runner = runner.next
        return self

dll = DoublyLinkedList()
dll.add_to_back("A").add_to_back("B").add_to_back("D")
dll.insert_before("C", "D")
dll.print_forward()  
print("---")
dll.print_backward() 
print("---")
dll.delete("B")
dll.print_forward()  