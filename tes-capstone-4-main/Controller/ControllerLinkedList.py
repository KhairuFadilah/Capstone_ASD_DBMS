from Model.Database import Database
from Model.Wisata import Wisata
from prettytable import PrettyTable
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def reset_data(self):
        self.head = None

    def refresh(self):
        self.reset_data()
        results = self.get_data()
        for result in results:
            id_wisata = result ["ID_Wisata"]
            nama_wisata = result ["Nama_Wisata"]
            deskripsi = result["Deskripsi"]  # Misalnya, deskripsi berada di indeks ke-1 dalam tuple
            lokasi = result["Lokasi"]     # Misalnya, lokasi berada di indeks ke-2 dalam tuple
            self.add_wisata(id_wisata, nama_wisata, deskripsi, lokasi)

    def get_data(self):
        db = Database()
        return db.get_wisata()

    def lihat_wisata(linked_list):
        current_node = linked_list.head
        while current_node:
            print("ID         :", current_node.id_wisata)
            print("Nama Wisata:", current_node.nama_wisata)
            print("Deskripsi  :", current_node.deskripsi)
            print("Lokasi     :", current_node.lokasi)
            print("--------------------------------------------------------------")
            current_node = current_node.next

    def add_wisata(self, id_wisata, nama_wisata, deskripsi, lokasi):
        wisata_baru = Wisata(id_wisata, nama_wisata, deskripsi, lokasi)
        if not self.head:
            self.head = wisata_baru
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = wisata_baru

    def delete_wisata(self, id_wisata):
        current_node = self.head
        if current_node and current_node.id_wisata == id_wisata:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_node.id_wisata != id_wisata:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        previous_node.next = current_node.next
        current_node = None

    def find_wisata(self, id_wisata):
        current_node = self.head
        while current_node:
            if current_node.id_wisata == id_wisata:
                return current_node
            current_node = current_node.next
        return None

    def update_wisata(self, id_wisata, nama_wisata, deskripsi, lokasi):
        current_node = self.find_wisata(id_wisata)
        if current_node:    
            if nama_wisata:
                current_node.nama_wisata = nama_wisata
            if deskripsi:
                current_node.deskripsi = deskripsi
            if lokasi:
                current_node.lokasi = lokasi
            print(f"Wisata dengan ID {id_wisata} telah diperbarui.")
        else:
            print(f"Wisata dengan ID {id_wisata} tidak ditemukan.")