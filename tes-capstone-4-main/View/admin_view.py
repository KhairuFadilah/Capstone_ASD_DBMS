from Controller.ControllerAccount import Account
from Controller.ControllerLinkedList import LinkedList
from Controller.ControllerSponsor import SponsorController
from Model.Database import Database
from View import user_view
from View import main_view
import os

acc = Account()
db = Database()
linked_list = LinkedList()
db.connect()

sponsor_controller = SponsorController()
linked_list = LinkedList()

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
                id_wisata = input("Masukan ID tempat wisata : ")
                nama_wisata = input("Masukan nama tempat wisata : ")
                lokasi = input("Masukan lokasi tempat wisata : ")
                deskripsi = input("Masukan deskripsi tempat wisata : ")
                linked_list.add_wisata(id_wisata, nama_wisata, lokasi, deskripsi)
                db.add_wisata(nama_wisata, deskripsi, lokasi)

            elif opsi == '2':
                os.system('cls')
                print("====================================")
                print("|        LIHAT TEMPAT WISATA       |")
                print("====================================")
                linked_list.refresh()
                linked_list.lihat_wisata()
                input("Tekan enter untuk kembali ke menu admin...")
                os.system('cls')
                menu_admin()

            elif opsi == '3':
                os.system('cls')
                print("====================================")
                print("|        EDIT TEMPAT WISATA        |")
                print("====================================")
                id_wisata = input("Masukan ID tempat wisata : ")
                nama_wisata = input("Masukan nama tempat wisata baru : ")
                lokasi = input("Masukan lokasi tempat wisata baru : ")
                deskripsi = input("Masukan deskripsi tempat wisata baru : ")
                linked_list.update_wisata(id_wisata, nama_wisata, deskripsi, lokasi)
                db.update_wisata(id_wisata, nama_wisata, deskripsi, lokasi)

            elif opsi == '4':
                os.system('cls')
                print("====================================")
                print("|        HAPUS TEMPAT WISATA       |")
                print("====================================")
                id_wisata = input("Masukan ID tempat wisata yang ingin dihapus: ")
                linked_list.delete_wisata(id_wisata)
                db.delete_wisata(id_wisata)

            elif opsi == '5':
                os.system('cls')
                print("====================================")
                print("|        CARI TEMPAT WISATA        |")
                print("====================================")
                search_query = input("Masukan nama atau lokasi wisata: ")
                pass

            elif opsi == '6':
                os.system('cls')
                print("====================================")
                print("|       URUTKAN TEMPAT WISATA      |")
                print("====================================")
                print(" [1] Urutkan berdasarkan nama wisata A-Z")
                print(" [2] Urutkan berdasarkan nama wisata Z-A")
                pilih = int(input("Pilih menu (1/2): "))
                if pilih == 1:
                    pass
                elif pilih == 2:
                    pass
                else:
                    print("Opsi tidak tersedia!")

            elif opsi == '7':
                print("====================================")
                print("|          HUBUNGI SPONSOR         |")
                print("====================================")
                print(" [1] Lihat daftar sponsor")
                print(" [2] Kirim permintaan kerja sama")
                pilih = int(input("Pilih menu (1/2): "))
                if pilih == 1:
                    sponsor_controller.lihat_sponsor()
                elif pilih == 2:
                    tanya_sponsor = input("apakah ingin menghubungi sponsor? (y/t) : ").lower()
                    if tanya_sponsor == 'y' :
                        jenis = input("Masukkan nama instansi atau perusahaan tujuan : ").capitalize()
                        kontak = input("Masukkan kontak sponsor : ")
                        alamat = input("Masukkan alamat : ")
                        bentuk = input("Deskripsikan bentuk kerja sama : ")
                        sponsor_controller.tambah_sponsor(jenis, kontak, alamat, bentuk)
                        print("   <<< Berhasil mengirim permintaan kerja sama >>>\n")
                    elif tanya_sponsor == 't':
                        break
                    else :
                        print("Opsi tidak tersedia!")
                else :
                    print("Opsi tidak tersedia!")
                
            elif opsi == '8':
                break
            else:
                print("Opsi tidak tersedia!")

    except KeyboardInterrupt:
        print("\nTerjadi Kesalahan!")
