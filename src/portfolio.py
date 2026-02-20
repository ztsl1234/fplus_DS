import logging

from src.transaction import Transaction, OperationType, ModeType
from src.queue import Queue

# Basic configuration to output to console
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

def simulate_portfolio(transactions: list[tuple[str, int, float, str]]) -> tuple[list[tuple[int, float]], float]:
    """
    Simulates a stock trading system with FIFO and LIFO modes.
    Returns the remaining inventory and total profit.
    """
    trn_objs=Transaction.load(transactions,"tuple_list")
    total_profit=0
    order_queue=Queue()
    for trn in trn_objs:
        trn.print()

        match trn.operation:
            case OperationType.BUY:
                if trn.mode.value==ModeType.FIFO.value:
                    order_queue.append_right((trn.shares, trn.price))
                elif trn.mode.value==ModeType.LIFO.value:
                    order_queue.append_right((trn.shares, trn.price))
            case OperationType.SELL:
                sell_trn_remaining_shares=trn.shares
                while sell_trn_remaining_shares != 0:
                    logging.info(f"DEBUG: trn.mode is {repr(trn.mode)} and ModeType.FIFO is {repr(ModeType.FIFO)}")
                    logging.info(trn.mode)
                    logging.info(ModeType.FIFO)
                    if trn.mode.value==ModeType.FIFO.value:
                        (buy_trn_shares, buy_trn_price)=order_queue.pop_left()
                        logging.info("FIFO")
                        logging.info(buy_trn_shares)
                    elif trn.mode.value==ModeType.LIFO.value:
                        (buy_trn_shares, buy_trn_price)=order_queue.pop_right()            
                        logging.info("LIFO")       
                        logging.info(buy_trn_shares)             
                    if buy_trn_shares <= sell_trn_remaining_shares:
                        sell_trn_remaining_shares -= buy_trn_shares

                        profit=(buy_trn_shares) * (trn.price - buy_trn_price)
                    else: #partial
                        buy_trn_remaining_shares = buy_trn_shares - sell_trn_remaining_shares
                        profit=sell_trn_remaining_shares * (trn.price - buy_trn_price)
                        sell_trn_remaining_shares=0
                        if trn.mode.value==ModeType.FIFO.value:
                            order_queue.append_right((buy_trn_remaining_shares, buy_trn_price))
                        elif trn.mode.value==ModeType.LIFO.value:
                            order_queue.append_right((buy_trn_remaining_shares, buy_trn_price))
                                            
                    total_profit += profit
            case _:
                raise ValueError("Unsupported Operation Type")

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
    logging.info(f"inventory={inventory}")
    logging.info(f"profit={total_profit}")
    (inventory,total_profit)=simulate_portfolio(transactions)
    logging.info(f"inventory={inventory}")
    logging.info(f"profit={total_profit}")