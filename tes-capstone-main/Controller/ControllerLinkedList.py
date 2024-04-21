from Model.Database import Database
from Model.Wisata import Wisata

from prettytable import PrettyTable

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Wisata(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node