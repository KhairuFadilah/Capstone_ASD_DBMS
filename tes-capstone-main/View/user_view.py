from Controller.ControllerAccount import Account
from Controller.ControllerUser import User
from View import admin_view
from View import main_view
import os

acc = Account()

def menu_user():
    while True :
        try :
            print("\n+--------------------------------------+")
            print("|            LOGIN PENGUNJUNG          |")
            print("+--------------------------------------+")
            print("|             1. registrasi            |")
            print("|             2. login                 |")
            print("|             3. keluar                |")
            print("+--------------------------------------+")
            pilihan = int(input("Masukkan pilihan anda : "))
            if pilihan == 1 :
                os.system("cls")
                regis_user()
            elif pilihan == 2 :
                login()
            elif pilihan == 3 :
                break
        except KeyboardInterrupt:
            print("tidak valid")

def regis_user():
    print("=====================================")
    print("            REGISTRASI AKUN          ")
    print("=====================================")
    while True:
        try:
            nama_user = input("Masukkan nama anda     : ").strip().capitalize()
            if all(x.isspace () for x in nama_user):
                print("> Nama tidak boleh kosong.")
            elif all(x.isnumeric () for x in nama_user):
                print("> Nama hanya boleh berisi huruf.")
            else:
                break
        except ValueError:
            print("> PERHATIKAN INPUT")
            
    while True:
        try:
            gender = input("Masukkan jenis kelamin : ").capitalize()
            if all(x.isspace() for x in gender):
                print("> Jenis kelamin tidak boleh kosong.")
            elif all(x.isnumeric() for x in nama_user):
                print("> Nama hanya boleh berisi huruf.")
            elif gender not in ['Pria, Wanita']:
                print("> Input harus berupa 'Pria' atau 'Wanita")
            else:
                break
        except ValueError:
            print("> PERHATIKAN INPUT")

    while True :
        try:
            usia_str = input("Masukkan usia          : ")
            if usia_str.strip() == "":
                print("> Usia tidak boleh kosong.")
            elif len(usia_str) > 3:
                print("perhatikan inputan")
            elif usia_str.isnumeric():
                usia = int(usia_str)
                last_visitor_id = acc.registrasi(nama_user, gender, usia)

            if last_visitor_id:
                print("     <<<  Registrasi berhasil!  >>>")
                print("         ID akun anda :", last_visitor_id)
                break
            else : 
                print("> Usia harus berupa angka.")
                break
        except KeyboardInterrupt:
            print("> PERHATIKAN INPUT")
            

def login():
    os.system("cls")
    print("========================================")
    print("                LOGIN AKUN             ")
    print("========================================")
    while True:
        try:
            login_user = str(input("Masukkan nama anda : ")).capitalize()
            id_user = int(input("Masukkan ID        : "))

            # Mencari nama pengguna dan ID pengguna di database
            account = Account()

            result = account.find_nama_id(login_user, id_user)
            if result:
                print("     <<<    Login berhasil!    >>>")
                print("     Selamat Datang,", login_user)

                menu_pengunjung()
                break
            else:
                print("> Nama atau ID salah!")
                print("> Silahkan coba lagi")
        except ValueError:
            print("terjadi kesalahan! ")

def menu_pengunjung():
        try:
            while True:
                print("\n+----------------------------------+")
                print("|           MENU PENGUNJUNG        |")
                print("+----------------------------------+")
                print("|                                  |")
                print("|         1. Cari Wisata           |")
                print("|         2. Lihat Wisata          |")
                print("|         3. Urutkan Wisata        |")
                print("|         4. Bookmark              |")
                print("|         5. keluar                |")
                print("|                                  |")
                print("+----------------------------------+")
                opsi = str(input("Pilih opsi anda (1/2/3/4/5): "))
                if opsi == '1':
                    os.system('cls')
                    pass
                elif opsi == '2':
                    os.system('cls')
                    pass
                elif opsi == '3':
                    os.system('cls')
                    pass
                elif opsi == '4':
                    os.system('cls')
                    pass
                elif opsi == '5':
                    menu_user()
                else:
                    print("Opsi tidak tersedia!")

        except KeyboardInterrupt:
            print("\nTerjadi Kesalahan!")
