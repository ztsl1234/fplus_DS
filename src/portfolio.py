import logging

from src.transaction import Transaction, OperationType, ModeType
from src.queue import Queue

MAX_TRANSACTIONS = 100000

# Basic configuration to output to console
logging.basicConfig
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(messages)'
)

logger=logging.getLogger(__name__)

__all__ = ['simulate_portfolio']  # ONLY this method will be exported

def simulate_portfolio(transactions: list[tuple[str, int, float, str]]) -> tuple[list[tuple[int, float]], float]:
    """
    Simulates a stock trading system with FIFO and LIFO modes.
    Returns the remaining inventory and total profit.
    """
    row_count=len(transactions)
    if row_count<1 :
        raise ValueError("There are no transactions to be loaded")
    elif row_count > MAX_TRANSACTIONS:
        raise ValueError(f"Exceeded limit of {MAX_TRANSACTIONS} transactions")
        
    trn_objs=Transaction.load(transactions,"tuple_list")
    total_profit=0.0
    inventory=Queue()
    for trn in trn_objs:
        trn.print()
        inventory.show()     

        match trn.operation:
            case OperationType.BUY:
                inventory.append_right((trn.shares, trn.price))
            case OperationType.SELL:
                total_profit=_sell_trn(trn,inventory)
            case _:
                raise ValueError("Unsupported Operation Type")

        inventory.show()     

    return (inventory, total_profit)

def _sell_trn(trn:Transaction, inventory: Queue) -> float:
    total_profit=0.0
    sell_trn_remaining_shares=trn.shares
    while sell_trn_remaining_shares != 0:
        if inventory.size()==0:
            logger.error(f"Short Sell : Need {sell_trn_remaining_shares} more shares")
            break
        
        index = 0 if trn.mode.value==ModeType.FIFO.value else -1
        (buy_trn_shares,buy_trn_price)=inventory.get(index)
        
        #check b4 pop
        if buy_trn_shares <= sell_trn_remaining_shares:                        
            sell_trn_remaining_shares -= buy_trn_shares
            profit=(buy_trn_shares) * (trn.price - buy_trn_price)
            
            inventory.pop_left() if trn.mode.value==ModeType.FIFO.value else inventory.pop_right()            
            
        else: #partial - do not pop, just update
            buy_trn_remaining_shares = buy_trn_shares - sell_trn_remaining_shares
            profit=sell_trn_remaining_shares * (trn.price - buy_trn_price)
            sell_trn_remaining_shares=0
            buy_trn_shares=buy_trn_remaining_shares
            updated_buy_tuple=(buy_trn_remaining_shares,buy_trn_price)

            inventory.put(index,updated_buy_tuple) 
            
        logging.info(f"profit={profit}")              
        logging.info(f"total_profit={total_profit}")              
        total_profit += profit

    return total_profit
    
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
        

