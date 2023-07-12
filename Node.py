class Node:
    def __init__(self,Key,Data,Next=None) -> None:
        self.Key = Key
        self.Data = Data
        self.Next = Next
    
    def __str__(self) -> str:
        return f"({self.Key}, {self.Data})"
    
    __repr__ = __str__