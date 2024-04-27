from Model.Database import Database
from Model.Wisata import Wisata
import os

db = Database()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_wisata(self, nama_wisata, deskripsi, lokasi):
        Wisata_baru = Wisata(nama_wisata, deskripsi, lokasi)
        if self.head is None:
            self.head = Wisata_baru
            self.tail = Wisata_baru
        else:
            Wisata_baru.previous = self.tail
            self.tail.next = Wisata_baru
            self.tail = Wisata_baru

    def find_wisata(self, nama_wisata):
        current = self.head
        while current:
            if current.nama_wisata == nama_wisata:
                return current
            current = current.next
        return None
    
    def get_wisata(self):
        data_wisata = db.get_wisata()

    def refresh(self):
        self.reset()
        result = self.get_wisata()
        for i in result:
            # Memasukan data kedalam node
            self.add_wisata(i[0], i[1], i[2], i[3])

    def reset(self):
        # Mengembalikan self.head menjadi None
        self.head = None

    def display(self):
        self.refresh()
        a = self.head
        if a is not None:
            print(f"ID Wisata : "[0], 
                    "Nama Wisata : "[1], 
                    "Deskripsi: "[2],
                    "Lokasi: "[3]
                    )

    def merge_sort(self, wisata, sort_by, ascending):
        if len(wisata) > 1:
            mid = len(wisata) // 2
            left_half = wisata[:mid]
            right_half = wisata[mid:]

            self.merge_sort(left_half, sort_by)
            self.merge_sort(right_half, sort_by)

            i = 0
            j = 0
            k = 0

            while i < len(left_half) and j < len(right_half):
                if sort_by == 'name':
                    if ascending:
                        if left_half[i].nama_wisata < right_half[j].nama_wisata:
                            wisata[k] = left_half[i]
                            i += 1
                        else:
                            wisata[k] = right_half[j]
                            j += 1
                    else:
                        if left_half[i].nama_wisata > right_half[j].nama_wisata:
                            wisata[k] = left_half[i]
                            i += 1
                        else:
                            wisata[k] = right_half[j]
                            j += 1
        return wisata