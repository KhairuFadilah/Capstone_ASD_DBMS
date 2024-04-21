class Wisata: #Node untuk menyimpan data tempat wisata
    def __init__(self, data):
        self.data = {"id_wisata"   : data[0],
                    "nama_wisata" : data[1],
                    "deskripsi"  : data[2],
                    "lokasi" : data[3]} 
        self.next = None