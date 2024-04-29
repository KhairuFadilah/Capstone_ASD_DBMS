from Controller.ControllerAccount import Account
from Model.Database import Database
from prettytable import PrettyTable

acc = Account()
db = Database()
db.connect()

class BookmarkController:
    def __init__(self):
        self.model = db

    def tambah_bookmark(self, tanggal_sekarang, wisata_bookmark, id_user):
        return self.model.tambah_bookmark(tanggal_sekarang, wisata_bookmark, id_user)

    def lihat_bookmark(self, user_id):
        bookmarks = self.model.lihat_bookmark(user_id)
        if bookmarks:
            bookmarks_tabel = PrettyTable(["ID", "Tanggal Ditambahkan", "Nama Wisata"])
            bookmarks_tabel.title = "Daftar Bookmark"
            for bookmark in bookmarks:
                bookmarks_tabel.add_row([bookmark[0], bookmark[1], bookmark[2]])
            print(bookmarks_tabel)
        else:
            print("Belum ada bookmark.")

    def find_bookmark(self, wisata_bookmark):
        return self.model.find_bookmark((wisata_bookmark,))
