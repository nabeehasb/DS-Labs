class Passenger:
    def __init__(self):  
        self.passenger = []  # to show at empty queue

    def insqueue(self,item):
        self.passenger.append(item) # appening it
        print(f"Enqueued passenger: {item}")

    def delqueue(self):
        if not self.is_empty():
            passenger = self.passenger.pop(0) #chaning is the queue is empty or not by applying the if condition
            return passenger
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.passenger) == 0 #to change the lenght of queuee

    def display(self):
        if not self.is_empty():
            print("Passengers are:")
            for passenger in self.passenger:
                print( passenger)
        else:
            print("Queue is empty")



queue = Passenger()

# now we will add the input 
queue.insqueue("Haris")
queue.insqueue("Amna")
queue.insqueue("Nabeeha")

# to call the queue
queue.display()
#now popping the passenger 
queue.delqueue()

# presenting the removes queue
queue.display()
