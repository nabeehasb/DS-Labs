def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.display()  # Display the stack after each push

def display(self):
    current = self.head
    elements = []
    while current:
        elements.append(current.data)
        current = current.next
    print("Stack:", " -> ".join(map(str, elements)))

stack=()
stack=(5,15,25,35)
stack.push(5,15,35)