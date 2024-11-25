#Lab Task - Even Roll No

#TASK 2
class Node: #we are making an queue
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:  #making a queue
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self): # apply the condition to check if it is empty
        return self.front is None

    def enqueue(self, data): # to add data in queue
        new_node = Node(data)
        if self.rear is None :
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self): # to remove data into queue
        if self.is_empty():
            print("Empty queue")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self): # to display the content
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None left")


queue = Queue()
queue.enqueue(22)
queue.enqueue(33)
queue.enqueue(44)
queue.enqueue(55)
queue.display()

print("Dequeued varable is : ", queue.dequeue()) #to print the queue
queue.display() # to display teh remaining data in the queue

#TASK 4

class Node:
    def __init__(self, data): # making a class named node 
        self.data = data
        self.next = None
class Queue:
    def __init__(self): #making a class names queue 
        self.front = None
        self.rear_node = None  
    
    def enqueue(self, data): # now we will enqueue to add data into the queue
        new_node = Node(data)
        if self.rear_node is None:  # If the queue is empty
            self.front = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
    
    def dequeue(self): # now will dequeue to remove data from queue
        if self.front is None:
            return None  # to check if the queue is empty or not
        temp = self.front
        self.front = temp.next
        
        if self.front is None:  # now the queue is empty
            self.rear_node = None
        
        return temp.data
    
    def rear(self): #rear is a method to return the last element without returning it
        if self.rear_node is None:
            return None  # empty queue
        return self.rear_node.data

q = Queue()
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)

print(q.rear())  # to print output
