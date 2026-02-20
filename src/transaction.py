
from dataclasses import dataclass
from enum import Enum
import pandas as pd
import os
from typing import Any, Dict
import logging

class OperationType(Enum):
    BUY="buy"
    SELL="sell"

class ModeType(Enum):
    FIFO="FIFO"
    LIFO="LIFO"

@dataclass
class Transaction:
    operation: OperationType
    shares:int
    price: float
    mode: ModeType
    
#load data from a list of tuple
    @classmethod
    def load_from_tuple(cls, data:tuple) -> "Transaction":
        return cls(operation=OperationType(data[0].lower()),
                shares=data[1],
                price=data[2],
                mode=ModeType(data[3].upper())
        )

    @classmethod
    def load_from_tuple_list(cls, data:list) -> list["Transaction"]:
        return [cls.load_from_tuple(t) for t in data]
        
    @classmethod
    def load_from_csv(cls, file_path:str) -> list["Transaction"]:
        df=pd.read_csv(file_path)
        df=pd.where(pd.notna(df),None)
        required_cols = ["operation", "shares", "price", "mode"]
        df=df[required_cols]
        return [ cls.load_from_dict(row) for row in df.to_dict('records')]

    @classmethod
    def load_from_dict(cls, data:Dict[str,Any]) -> "Transaction":
        return cls(operation=data["operation"],
                shares=int(data["shares"]),
                price=float(data["price"]),
                model=data["mode"])
    @classmethod
    def load(cls, source: Any,source_type: str) -> list["Transaction"]:
        match source_type:
            case "csv":
                return cls.load_from_csv(source)
            case "tuple_list":
                return cls.load_from_tuple_list(source)
   
    def print(self):
        logging.info(self.operation)
        logging.info(self.shares)
        logging.info(self.price)
        logging.info(self.mode)
        logging.info("-----------------------")
    
    #validation            
    #def __post_init__():
        