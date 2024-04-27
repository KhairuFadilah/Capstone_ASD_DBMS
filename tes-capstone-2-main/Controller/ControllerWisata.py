from Model.Database import Database

class HistoryWisata:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

class WisataController:
    def __init__(self, database):
        self.db = database
        
    def add_wisata(linked_list, nama_wisata, lokasi, deskripsi):
        linked_list.add_wisata(nama_wisata, deskripsi, lokasi)
    
    def get_wisata(linked_list):
        return linked_list.to_list()
    def update_wisata(linked_list, wisata_id, nama_wisata, lokasi, deskripsi):
        node = linked_list.find(lambda x: x.wisata_id == wisata_id)
        if node:
            if nama_wisata:
                node.data.nama_wisata = nama_wisata
            if lokasi:
                node.data.lokasi = lokasi
            if deskripsi:
                node.data.deskripsi = deskripsi
    
    def delete_wisata(linked_list, wisata_id):
        linked_list.remove(lambda x: x.wisata_id == wisata_id)
    
    def sync_with_database(linked_list, database):
        database.clear_wisata()  # Assuming a method to clear the wisata table
        current = linked_list.head
        while current:
            database.add_wisata(current.data.nama_wisata, current.data.lokasi, current.data.deskripsi)
            current = current.next

    def search_wisata(self, search_query):
        results = self.db.search_wisata(search_query)
        if results:
            for result in results:
                print(f"ID: {result[0]}, Nama: {result[1]}, Lokasi: {result[2]}, Deskripsi: {result[3]}")
        else:
            print("No matching wisata found.")
    
    # def show_sorted_wisata_ascending(self):
    #     results = self.db.get_sorted_wisata_ascending()
    #     if results:
    #         for result in results:
    #             print(f"ID: {result[0]}\nNama: {result[1]}\nLokasi: {result[2]}\nDeskripsi: {result[3]}\n")
    #     else:
    #         print("Tidak ada wisata yang tersedia.")

    
    # def show_sorted_wisata_descending(self):
    #     results = self.db.get_sorted_wisata_descending()
    #     if results:
    #         for result in results:
    #             print(f"ID: {result[0]}\nNama: {result[1]}\nLokasi: {result[2]}\nDeskripsi: {result[3]}\n")
    #     else:
    #         print("Tidak ada wisata yang tersedia.")