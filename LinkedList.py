from Node import Node
import copy

class LinkedList:
    def __init__(self) -> None:
        self.HeadNode = None

    def Insert(self,NodeToInsert:Node):
        NodeToInsert.Next = self.HeadNode
        self.HeadNode = NodeToInsert
    
    def Search(self,Key):
        CurrentNode = self.HeadNode
        while CurrentNode != None and CurrentNode.Key != Key:
            CurrentNode = CurrentNode.Next
        return CurrentNode
    
    def printSelf(self):
        CurrentNode = self.HeadNode
        Output = ""
        while CurrentNode.Next != None:
            Output = Output + f"{CurrentNode} -> "
            CurrentNode = CurrentNode.Next
        Output = Output + f"{CurrentNode}"
        print(Output)