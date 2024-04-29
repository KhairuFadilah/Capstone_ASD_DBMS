class Wisata: #Node untuk menyimpan data tempat wisata
    def __init__(self, id_wisata, nama_wisata, deskripsi, lokasi):
        self.id_wisata = id_wisata
        self.nama_wisata = nama_wisata
        self.deskripsi = deskripsi
        self.lokasi = lokasi
        self.next = None
        self.previous = None
