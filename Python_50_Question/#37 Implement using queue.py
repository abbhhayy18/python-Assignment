""" . Implement Queue using List  
● Create a queue with enqueue, dequeue, and peek operations using a list. 
Example Scenario  
1. Enqueue Operations:  
o Add elements to the queue in the order: 10, 20, 30.  
2. Dequeue Operation: 
o Remove the front element of the queue (FIFO principle). 
3. Peek Operation:  
o View the element at the front of the queue without removing it. 
Expected Output  
Given the above operations, the sequence would look like this:  
● After enqueuing 10, 20, and 30:  
Queue: [10, 20, 30]  
● After calling peek (without removing any item):  
Output: 10  
● After calling dequeue twice:  
Queue: [30]  
● After calling peek again:  
Output: 30  
● After calling dequeue one more time (emptying the queue): 
Queue: []  
● If attempting to dequeue on an empty queue:  
Output: "Queue is empty, cannot dequeue."""

class IMPLEMENT_QUEUE:
    def __init__(self,queue):
        self.queue = queue

    def append(self,item):
        self.queue.append(item)
    

    def dequeue(self):
        if len(queue) > 0:
            print(" calling dequeue... ")
            self.queue.pop(0)
        else:
             print("Queue is empty, cannot dequeue.")
       

    def peek(self):
        if len(queue) > 0:
            print(f" Peek element is :{self.queue[0]}")
        else:
            print(f"Queue:{queue}")
        

if __name__ == "__main__": # This line is used to check whether a python file is being run   directly or being imported as a module
    queue=[]
    obj = IMPLEMENT_QUEUE(queue)
    obj.append(10)
    obj.append(20)
    obj.append(30)

    obj.peek()
    obj.dequeue()
    obj.peek()
    obj.dequeue()
    obj.dequeue()
    obj.peek()
    obj.dequeue()
