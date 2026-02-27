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
    
    def get(self,index):
        return self.container[index]

    def put(self,index,item):
        self.container[index]=item
        
    def show(self):
        return list(self.container)       
        
    