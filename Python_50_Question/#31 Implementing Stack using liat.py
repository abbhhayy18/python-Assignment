""" . Implement a Stack using List  
● Create a stack with push, pop, and peek operations using a list.  
Stack: A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means that the last 
element added to the stack is the first one to be removed. Think of it like a stack of plates; you can only add or 
remove plates from the top.  
List: A list is a more general data structure that can store a collection of items. It allows for random access and 
can be used to store elements in any order. Lists do not have strict rules about how elements are added or 
removed.  
● Example:  
Stack Operations: 
● Push: stack.push(10)  
● Push: stack.push(20)  
● Push: stack.push(30)  
● Peek: stack.peek()  
Expected Output: 30  
● Pop: stack.pop()  
Expected Output: 30  
● Peek: stack.peek()  
Expected Output: 20  
● Pop: stack.pop()  
Expected Output: 20  
● Pop: stack.pop()  
Expected Output: 10  
● Pop: stack.pop()  
Expected Output: None (or an indication that the stack is empty)  """

class STACK:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(self.stack)

    def peek(self):
        if self.is_empty():
            return f"The peek element is {self.stack[-1]}"
        return none
    
    def pop(self):
        if self.is_empty():
            return f"removing element-{self.stack.pop()}" # removing last inserted element
        return "Now the Stack is empty"

    def is_empty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True

obj = STACK()
obj.push(10)
obj.push(20)
obj.push(30)

print(obj.peek())
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.pop())
print(obj.pop())

