from Controller.ControllerAccount import Account
from Controller.ControllerLinkedList import LinkedList
from Controller.ControllerWisata import WisataController
from Model.Database import Database
from View import user_view
from View import main_view
import os

ll = LinkedList()
acc = Account()
db = Database()
db.connect()
wisata_controller = WisataController(db)

def login_admin():
    while True :
        try :
            print("===================================")
            print("            LOGIN ADMIN           ")
            print("===================================")
            username = str(input("Masukan Username : "))
            password= int(input("Masukan Password : "))
            account = Account()

            result = account.find_admin (username, password)
            if result:
                print("     <<<    Login berhasil!    >>>\n")
                menu_admin()
                break
            else:
                print("Nama pengunjung atau ID tidak cocok.")

        except KeyboardInterrupt:
            print("tidak valid")

def menu_admin():
        try:
            while True:
                print("+----------------------------------+")
                print("|            MENU ADMIN            |")
                print("+----------------------------------+")
                print("|                                  |")
                print("|         1. Tambah Wisata         |")
                print("|         2. Lihat Wisata          |")
                print("|         3. Edit Wisata           |")
                print("|         4. Hapus Wisata          |")
                print("|         5. Cari Wisata           |")
                print("|         6. Urutkan Wisata        |")
                print("|         7. Hubungi Sponsor       |")
                print("|         8. keluar                |")
                print("|                                  |")
                print("+----------------------------------+")
                opsi = str(input("Pilih opsi anda (1/2/3/4/5): "))

                if opsi == '1':
                    os.system('cls')
                    nama_wisata = input("Masukan nama tempat wisata : ")
                    lokasi = input("Masukan lokasi tempat wisata : ")
                    deskripsi = input("Masukan deskripsi tempat wisata : ")
                    wisata_controller.add_wisata(nama_wisata, lokasi, deskripsi)
                    print("Tempat wisata telah ditambahkan!")
                    pass
                elif opsi == '2':
                    os.system('cls')
                    id_wisata = input("Masukan ID tempat wisata (Kosongkan untuk melihat semua tempat wisata) : ")
                    if id_wisata:
                        wisata = wisata_controller.get_wisata(id_wisata)
                    else:
                        wisata = wisata_controller.get_wisata()
                elif opsi == '3':
                    os.system('cls')
                    id_wisata = input("Masukan ID tempat wisata : ")
                    nama_wisata = input("Masukan nama tempat wisata baru (Kosongkan untuk tidak merubah nama) : ")
                    lokasi = input("Masukan lokasi tempat wisata baru (Kosongkan untuk tidak merubah lokasi) : ")
                    deskripsi = input("Masukan deskripsi tempat wisata baru (Kosongkan untuk tidak merubah deskripsi) : ")
                    wisata_controller.edit_wisata(id_wisata, nama_wisata, lokasi, deskripsi)
                    pass
                elif opsi == '4':
                    os.system('cls')
                    id_wisata = input("Masukan ID tempat wisata yang ingin dihapus: ")
                    wisata_controller.delete_wisata(id_wisata)
                    print("Tempat wisata telah dihapus!")
                    pass
                elif opsi == '5':
                    search_query = input("Masukan nama atau lokasi wisata: ")
                    wisata_controller.search_wisata(search_query)
                    pass
                elif opsi == '6':
                    print("1. Ascending")
                    print("2. Descending")
                    pilih = int(input("Pilih menu (1/2): "))
                    if pilih == 1:
                        wisata_controller.show_sorted_wisata_ascending()
                    elif pilih ==2:
                        wisata_controller.show_sorted_wisata_descending()
                    else:
                        print("Opsi tidak tersedia!")
                    pass
                elif opsi == '7':
                    pass
                elif opsi == '8':
                    pass
                else:
                    print("Opsi tidak tersedia!")

        except KeyboardInterrupt:
            print("\nTerjadi Kesalahan!")

def create():
    print("====================================")
    print("|       TAMBAH TEMPAT WISATA       |")
    print("====================================")
    

