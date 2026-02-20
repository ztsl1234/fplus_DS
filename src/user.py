from dataclasses import dataclass
from typing import Any, Dict
import json
import os
import pandas as pd

@dataclass
class User:
    id:int
    name:str
    email:str
    age:int|None = None #optional, default to none

    @classmethod
    #for structured data
    def from_dict(cls,data:Dict[str,Any]) -> "User":
        return cls(id=int(data["id"]),
                   name=str(data["name"]),
                   email=data["email"],
                   age=data.get("age"), #optional
        )
    @classmethod
    def from_json_file(cls,path:str) -> "User":
        with open(path, "r", encoding="utf-8") as f:
            return(cls.from_dict(json.load(f))      
        )

    @classmethod
    def from_json(cls, json_str: str) -> "User":
        return(cls.from_dict(json.loads(json_str)))
    
    @classmethod
    #from csv
    def from_csv_file(cls, path:str) -> list["User"]:
        df=pd.read_csv(path)
        # Replace NaN (Not a Number) with None so your dataclass stays clean
        df = df.where(pd.notna(df), None)
        
        # Convert each row (record) into a User object
        return [cls.from_dict(row) for row in df.to_dict('records')]
    
    def from_csv(cls, rows:Dict[str,str]) -> "User":
        return cls(id=int(rows["id"]), 
                   name=rows["name"],
                   email=rows["email"],
                   age=int(rows.get("age")) if rows.get("age") is not None else None
        )
    
    @classmethod
    def load(cls, source: Any, source_type:str) -> "User":
        #python 3.10 match
        match source_type:
            case "dict":
                return cls.from_dict(source)
            case "csv":
                return cls.from_csv(source)
            case "json":
                return cls.from_json(source)
            case "json_file":
                return cls.from_json_file(source)
            case _:
                raise ValueError("Unsupported Source type")

    