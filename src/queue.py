from collections import deque 
import logging

class Queue:
    def __init__(self):
        #double ended q, double linked list
        #o(1) time complexity for appends and pop on both ends
        self.queue = deque() 
        
    def peek(self):
        return self.queue[-1] if self.queue else None
    
    def size(self):
        return len(self.queue)
    
    def append_right(self,item):
        self.queue.append(item) #append to right end
        
    def pop_right(self):
        return self.queue.pop() #remove from right end

    def pop_left(self):
        return self.queue.popleft() #remove from left end
    
    def get(self,index):
        return self.queue[index]

    def put(self,index,item):
        self.queue[index]=item
        
    def to_list(self):
        return list(self.queue)       
        
    def show(self):
        print(f"Queue : {list(self.queue)}")       
    