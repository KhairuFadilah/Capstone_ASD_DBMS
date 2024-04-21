from Model import Database
from Model.Database import Database

class Account():

    def __init__(self):
        self.model = Database()
        self.model.connect()

    def registrasi(self, nama_user, gender, usia):
        # Memanggil metode registrasi dari ModelDatabase untuk menambahkan pengguna baru
        last_visitor_id = self.model.registrasi(nama_user, gender, usia)
        return last_visitor_id
    
    def find_nama_id(self, nama_user, id_user):
        # Panggil metode find_nama_id dari ModelDatabase untuk mencari pengunjung
        return self.model.find_nama_id(nama_user, id_user)
    
    def find_admin(self, username, password):
        return self.model.find_admin(username, password)