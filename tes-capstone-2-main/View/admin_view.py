from Controller.ControllerAccount import Account
from Controller.ControllerWisata import WisataController
from Controller.ControllerLinkedList import LinkedList
from Model.Database import Database
from View import user_view
from View import main_view
import os

acc = Account()
wisata_controller = WisataController()
wisata_linkedlist = LinkedList()
db = Database(wisata_linkedlist)
db.connect()

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
                opsi = str(input("Pilih opsi anda (1/2/3/4/5/6/7/8): "))

                if opsi == '1':
                    os.system('cls')
                    print("====================================")
                    print("|       TAMBAH TEMPAT WISATA       |")
                    print("====================================")
                    nama_wisata = input("Masukan nama tempat wisata : ")
                    lokasi = input("Masukan lokasi tempat wisata : ")
                    deskripsi = input("Masukan deskripsi tempat wisata : ")
                    wisata_controller.add_wisata(nama_wisata, lokasi, deskripsi)
                    print("Tempat wisata telah ditambahkan!")

                elif opsi == '2':
                    os.system('cls')
                    print("====================================")
                    print("|        LIHAT TEMPAT WISATA       |")
                    print("====================================")
                    wisata_list = wisata_controller.get_all_wisata()  # Assuming this method now pulls from the linked list
                    for wisata in wisata_list:
                        print(f"ID: {wisata.id}, Name: {wisata.nama_wisata}, Location: {wisata.lokasi}, Description: {wisata.deskripsi}")

                elif opsi == '3':
                    os.system('cls')
                    print("====================================")
                    print("|        EDIT TEMPAT WISATA        |")
                    print("====================================")
                    id_wisata = input("Masukan ID tempat wisata : ")
                    nama_wisata = input("Masukan nama tempat wisata baru (Kosongkan untuk tidak merubah nama) : ")
                    lokasi = input("Masukan lokasi tempat wisata baru (Kosongkan untuk tidak merubah lokasi) : ")
                    deskripsi = input("Masukan deskripsi tempat wisata baru (Kosongkan untuk tidak merubah deskripsi) : ")
                    wisata_controller.update_wisata(id_wisata, nama_wisata, lokasi, deskripsi)

                elif opsi == '4':
                    os.system('cls')
                    print("====================================")
                    print("|        HAPUS TEMPAT WISATA       |")
                    print("====================================")
                    id_wisata = input("Masukan ID tempat wisata yang ingin dihapus: ")
                    wisata_controller.delete_wisata(id_wisata)
                    print("Tempat wisata telah dihapus!")

                elif opsi == '5':
                    os.system('cls')
                    print("====================================")
                    print("|        CARI TEMPAT WISATA        |")
                    print("====================================")
                    search_query = input("Masukan nama atau lokasi wisata: ")
                    wisata_controller.search_wisata(search_query)

                elif opsi == '6':
                    os.system('cls')
                    print("====================================")
                    print("|       URUTKAN TEMPAT WISATA      |")
                    print("====================================")
                    print(" [1] Urutkan berdasarkan nama wisata A-Z")
                    print(" [2] Urutkan berdasarkan nama wisata Z-A")
                    pilih = int(input("Pilih menu (1/2): "))
                    if pilih == 1:
                        wisata_data = wisata_linkedlist.get_wisata()
                        sorted_wisata = wisata_linkedlist.merge_sort(wisata_data, 'name', ascending=True)
                    elif pilih ==2:
                        wisata_linkedlist.merge_sort("name", descending=False)
                    else:
                        print("Opsi tidak tersedia!")

                elif opsi == '7':
                    print("====================================")
                    print("|          HUBUNGI SPONSOR         |")
                    print("====================================")
                    pass
                elif opsi == '8':
                    break
                else:
                    print("Opsi tidak tersedia!")

        except KeyboardInterrupt:
            print("\nTerjadi Kesalahan!")
