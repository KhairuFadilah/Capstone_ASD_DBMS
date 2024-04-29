from Model import Database
from Model.Database import Database
from prettytable import PrettyTable

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
        # Panggil metode find_admin dari ModelDatabase untuk mencari admin
        return self.model.find_admin(username, password)

    def find_profil(self, id_user):
        pengunjung = self.model.find_profil(id_user)
        if pengunjung:
            profil_tabel = PrettyTable(["ID Pengunjung", "Nama", "Jenis Kelamin", "Usia"])
            profil_tabel.title = "Profil Pengunjung"
            profil_tabel.add_row([pengunjung["ID_Pengunjung"], pengunjung["Nama_Pengunjung"], pengunjung["Jenis_Kelamin"], pengunjung["Umur"]])
            print(profil_tabel)
        else:
            print("Pengunjung tidak ditemukan.")

            
