#Task 1:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#as mentioned we will make a new class names node to store values in it

class stack:
    def __init__(self):
        self.head = None
#make a new class names stack to store value and in the second line checking the status of the stack


    def push(self, data):
        new_node = Node(data) # creating a new node
        new_node.next = self.head
        self.head = new_node
        self.display()  # Display the stack 

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
            print("Stack:", " -> ".join(map(str, elements)))

stack = stack()
stack.push(5)
stack.push(15)
stack.push(25)
stack.push(35)

#Tak 2:
class Node:
    def __init__(self, item):
        self.item = item  
        self.next = None  
#as mentioned we will make a new class names node to store values in it

#make a new class names stack to store value and in the second line checking the status of the stack

class Stack:
    def __init__(self):
        self.head = None  

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.display()

    def pop(self):
 # Check if the stack is empty
        if self.head is None:
            print("Stack Underflow")
            return None
        popped_data = self.head.item
        self.head = self.head.next
        self.display()  # Display the stack after each pop
        return popped_data

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.item)
            current = current.next
        if elements:
            print("Stack:", " -> ".join(map(str, elements)))
        else:
            print("Stack is empty!")


# Initialize the stack
stack = Stack()

# Push elements
stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)

# Pop elements
stack.pop()  
stack.pop()  
stack.pop()  
stack.pop()  
stack.pop()  
#popping until empty


#Task 3:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#as mentioned we will make a new class names node to store values in it

class Stack:
#make a new class names stack to store value and in the second line checking the status of the stack

    def __init__(self):
        self.head = None
    
    def push(self,data): #push the dat in new_node
        new_node = Node(data)
        new_node.next= self.head
        self.head = new_node
        self.display()

    def pop(self): #defing pop and check if it is empty
        if self.head is None:
            print("Empty stack")
        else:
            popped_node = self.head
            self.head = self.head.next 
            print(f"pooped stack",popped_node)
            self.display()
    
    def peek(self): #peek def and checking if it is empty or not
        if self.head is None:
            print("Empty stack")
        else:
            print(f"Top elemment",self.head.data)
    
    def display(self): #displaying the data
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        if elements:
            print("Stack:", " -> ".join(map(str, elements)))
        else:
            print("empty stack")

# Initialize the stack
stack = Stack()
#pushing the stack
stack.push(12)
stack.push(22)
stack.push(32)
stack.push(42)

#peeking it now
stack.peek()

#Task 4:
class Node:
#as mentioned we will make a new class names node to store values in it

    def __init__(self,data):
        self.data = data()
        self.next = None

class Stack:
#make a new class names stack to store value and in the second line checking the status of the stack

    def __init__(self):
        self.head=None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.display()

    def pop(self):
        if self.head is None:
            print("stack is underflow")
        else:
            pooped_node = self.head
            self.head = self.head.next
            print(f"popped",pooped_node.data)
    
    def peek(self):
        if self.head is None:
            print("empty stack")
        else:
            print(f"top element", self.head.data)
    
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        if elements:
            print("Stack:", " -> ".join(map(str, elements)))
        else:
            print("Empty stack")

# Initialize the stack
stack = Stack()
#popping th stack
stack.pop()

