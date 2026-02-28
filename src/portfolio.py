import logging

from src.transaction import Transaction, OperationType, ModeType
from src.queue import Queue

MAX_TRANSACTIONS = 100000

# Basic configuration to output to console
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
__all__ = ['simulate_portfolio']  # ONLY this will be exported

def simulate_portfolio(transactions: list[tuple[str, int, float, str]]) -> tuple[list[tuple[int, float]], float]:
    """
    Simulates a stock trading system with FIFO and LIFO modes.
    Returns the remaining inventory and total profit.
    """
    if len(transactions)<1 :
        raise ValueError("There are no transactions to be loaded")
    elif len(transactions) > MAX_TRANSACTIONS:
        raise ValueError(f"Only {MAX_TRANSACTIONS} transactions can be loaded")
        
    trn_objs=Transaction.load(transactions,"tuple_list")
    total_profit=0
    order_queue=Queue()
    for trn in trn_objs:
        trn.print()
        order_queue.show()     

        match trn.operation:
            case OperationType.BUY:
                if trn.mode.value==ModeType.FIFO.value:
                    order_queue.append_right((trn.shares, trn.price))
                elif trn.mode.value==ModeType.LIFO.value:
                    order_queue.append_right((trn.shares, trn.price))
            case OperationType.SELL:
                sell_trn_remaining_shares=trn.shares
                while sell_trn_remaining_shares != 0:
                    logging.debug(trn.mode)
                    logging.info(f"size={order_queue.size()}")
                    if order_queue.size()==0:
                        break
                    
                    if trn.mode.value==ModeType.FIFO.value:
                        (buy_trn_shares,buy_trn_price)=order_queue.get(0)
                    elif trn.mode.value==ModeType.LIFO.value:
                        (buy_trn_shares,buy_trn_price)=order_queue.get(-1)
                    
                    #check b4 pop
                    if buy_trn_shares <= sell_trn_remaining_shares:                        
                        sell_trn_remaining_shares -= buy_trn_shares
                        profit=(buy_trn_shares) * (trn.price - buy_trn_price)
                        #pop!
                        if trn.mode.value==ModeType.FIFO.value:
                            (buy_trn_shares, buy_trn_price)=order_queue.pop_left()
                        elif trn.mode.value==ModeType.LIFO.value:
                            (buy_trn_shares, buy_trn_price)=order_queue.pop_right()            
                        
                    else: #partial - do not pop, just update
                        buy_trn_remaining_shares = buy_trn_shares - sell_trn_remaining_shares
                        profit=sell_trn_remaining_shares * (trn.price - buy_trn_price)
                        sell_trn_remaining_shares=0
                        buy_trn_shares=buy_trn_remaining_shares
                        updated_buy_tuple=(buy_trn_remaining_shares,buy_trn_price)
    
                        if trn.mode.value==ModeType.FIFO.value:
                            order_queue.put(0,updated_buy_tuple)
                        elif trn.mode.value==ModeType.LIFO.value:
                            order_queue.put(-1,updated_buy_tuple)
                              
                    logging.info(f"profit={profit}")              
                    logging.info(f"total_profit={total_profit}")              
                    total_profit += profit
            case _:
                raise ValueError("Unsupported Operation Type")

        order_queue.show()     

    order_queue.show()     

    return (order_queue, total_profit)
  
if __name__ == "__main__":

    transactions = [ ("buy", 100, 10.0, "FIFO"), 
                    ("buy", 50, 12.0, "FIFO"), 
                    ("sell", 80, 15.0, "FIFO"),
                    ("buy", 30, 14.0, "LIFO"), 
                    ("sell", 40, 16.0, "LIFO"), 
                    ("buy", 20, 11.0, "FIFO"), 
                    ("sell", 20, 13.0, "FIFO") ]
    inventory=[]
    total_profit=0
    print(f"inventory={inventory}")
    print(f"profit={total_profit}")
    (inventory,total_profit)=simulate_portfolio(transactions)
    print(f"Remaining positions ={inventory.show()}")
    print(f"Total_profits={total_profit}")
        
    transactions = [ ("buy", 50, 10.0, "FIFO"), ("buy", 60, 10.0, "FIFO"), ("sell", 100, 5.0, "FIFO") ]

    inventory=[]
    total_profit=0
    print(f"inventory={inventory}")
    print(f"profit={total_profit}")
    (inventory,total_profit)=simulate_portfolio(transactions)
    inventory.show()
    print(f"Remaining positions ={inventory.show()}")
    print(f"Total_profits={total_profit}")
        
    transactions = [ ("buyx", 50.0, 10, "FIFO"), ("buy", 0, 10.0, "FIFO"), ("sell", 100, 0, "FIFO"),("buy", 100, 9.0, "LIFO"),("buy", 50, 11.0, "LIFO"),("sell", 1000, 15.0, "FIFO") ]

    inventory=[]
    total_profit=0
    print(f"inventory={inventory}")
    print(f"profit={total_profit}")
    (inventory,total_profit)=simulate_portfolio(transactions)
    inventory.show()
    print(f"Remaining positions ={inventory.show()}")
    print(f"Total_profits={total_profit}")
        

