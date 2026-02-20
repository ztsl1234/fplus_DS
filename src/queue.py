from collections import deque 
import logging

class Queue:
    def __init__(self):
        self.container = deque() #double ended q, double linked list
        
    def peek(self):
        return self.container[-1] if self.container else None
    
    def size(self):
        return len(self.container)
    
    def append_right(self,val):
        self.container.append(val) #append to right end
        
    def pop_right(self):
        return self.container.pop() #remove from right end

    def pop_left(self):
        return self.container.popleft() #remove from left end
        
    def show(self):
        logging.info(f"{self.container}")             
        
    