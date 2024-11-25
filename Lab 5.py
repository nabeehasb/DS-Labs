#Task 1:-

class Node:
    def __init__(self, data):
        self.data = data  
        self.prev = None 
        self.next = None  

# to insert a node at the end of the doubly linked list we use push function
def push(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    
    # move to the end of the list
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head

# to remove the last node from the doubly linked list we use pop function
def pop(head):
    if not head:
        print("List empty")
        return None
    if not head.next:
        return None
    current = head  # move to the last node
    while current.next:
        current = current.next
    current.prev.next = None
    
    return head

# to insert a node at a specific position in the doubly linked list
def insert(head, data, position):
    new_node = Node(data)      
    if position == 0:  # inserting at position 0
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node
    
    current = head
    for i in range(position - 1):
        if not current:
            print("Position out of range")
            return head
        current = current.next
    
    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    new_node.prev = current
    
    return head

# to delete a node at a specific position in the doubly linked list
def delete_node(head, position):
    if not head:
        print("List is empty")
        return None
    if position == 0:
        next_node = head.next
        if next_node:
            next_node.prev = None
        head = next_node  # Update the head of the list
        return head
    
    current = head
    for i in range(position):
        if not current: 
            print("Position is out of range")
            return head
        current = current.next

    if current.prev:
        current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev

    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")



head = None

#push nodes to the list
head = push(head, 12)
head = push(head, 23)
head = push(head, 355)
head = push(head, 678)
head = push(head, 33)

print("Original list is:")
print_list(head)

# Insert a node at position 2
head = insert(head, 6, 2)
print("\nList after inserting 6 at position 2:")
print_list(head)

# Pop (remove) the last node
head = pop(head)
print("\nList after popping the last node:")
print_list(head)

# Delete a node at position 2
head = delete_node(head, 2)
print("\nList after deleting node at position 2:")
print_list(head)



#Task 2:-



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
   
    def append(self, data):# to insert a node at the end of a circular linked list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):#to print the circular linked list
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def split_list(self): #to split the circular linked list into two halves

        if not self.head or self.head.next == self.head:
            return None, None
        
        slow_ptr = self.head
        fast_ptr = self.head
        
        while fast_ptr.next != self.head and fast_ptr.next.next != self.head:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        head1 = self.head
        head2 = slow_ptr.next

        slow_ptr.next = head1
        
        temp = head2
        while temp.next != self.head:
            temp = temp.next
        temp.next = head2
        
        return head1, head2

def print_circular_list(head): # to print
    if not head:
        return
    temp = head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == head:
            break
    print()

cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.append(5)

print("Original Circular Linked List is:")
cll.print_list()

# Split the list
head1, head2 = cll.split_list()

print("\nFirst Half is:")
print_circular_list(head1)

print("\nSecond Half is:")
print_circular_list(head2)
