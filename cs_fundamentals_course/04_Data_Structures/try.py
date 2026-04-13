class Node:
    def __init__(self,value , next=None):
        self.value = value
        self.next = next 


class LinkeList:
    def __init__(self):
        self.head = None 

    def insert_head(self, value):
        self.head = Node(value)
        