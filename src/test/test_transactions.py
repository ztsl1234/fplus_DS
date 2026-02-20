import pytest
from src.transaction import Transaction
from src.queue import Queue
from src.transaction import OperationType
from src.transaction import ModeType
import logging

@pytest.fixture
def transactions1():
    transactions = [ ("buy", 100, 10.0, "FIFO"), ("buy", 50, 12.0, "FIFO"), ("sell", 80, 15.0, "FIFO"), ("buy", 30, 14.0, "LIFO"), ("sell", 40, 16.0, "LIFO"), ("buy", 20, 11.0, "FIFO"), ("sell", 20, 13.0, "FIFO") ]

    return Transaction.load(transactions,"tuple_list")

def test_trans(transactions1):
    for t in transactions1:
        t.print()
        
def test_queue(transactions1):
    order_queue=Queue()
    for t in transactions1:
        match t.operation:
            case OperationType.BUY:
                if t.mode==ModeType.FIFO:
                    order_queue.push((t.shares, t.price))
                else:
                    order_queue.push((t.shares, t.price))
            case OperationType.SELL:
                if t.mode==ModeType.FIFO:
                    order_queue.pop((t.shares, t.price))
                else:
                    order_queue.pop((t.shares, t.price))        
    
    order_queue.show()     