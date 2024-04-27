class Wisata: #Node untuk menyimpan data tempat wisata
    def __init__(self, id_wisata, nama_wisata, deskripsi, lokasi):
        self.id_wisata = id_wisata
        self.nama_wisata = nama_wisata
        self.deskripsi = deskripsi
        self.lokasi = lokasi
        self.next = None
        self.previous = None

class ListWisata:
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
