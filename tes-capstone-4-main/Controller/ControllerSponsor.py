from Controller.ControllerAccount import Account
from Model.Database import Database
from prettytable import PrettyTable

db = Database()
db.connect()


class SponsorController:
    def __init__(self):
        self.model = db

    def tambah_sponsor(self, jenis, kontak, alamat, bentuk):
        return self.model.tambah_sponsor(jenis, kontak, alamat, bentuk)

    def lihat_sponsor(self):
        results = self.model.lihat_sponsor()
        for result in results:
            if result:
                print(f"ID: {result[0]}\nNama Sponsor: {result[1]}\n{result[2]}\nAlamat: {result[3]}\nBentuk Sponsor: {result[4]}\n")
            else:
                print("Belum ada sponsor.")
