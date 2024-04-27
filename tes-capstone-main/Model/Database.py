import mysql.connector

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="",   
            database="Wisata_kaltim" 
        )
        myCursor = self.connection.cursor() 
        myCursor.execute("USE Wisata_Kaltim")

    def find_nama_id(self, nama_user, id_user):
        query = "SELECT * FROM Pengunjung WHERE Nama_Pengunjung = %s AND ID_Pengunjung = %s"
        values = (nama_user, id_user)
        
        myCursor = self.connection.cursor() 
        myCursor.execute(query, values)  # Eksekusi kueri dengan menggunakan variabel values
        myresult = myCursor.fetchall()   # Ambil hasil dari kueri
        
        return myresult  # Mengembalikan hasil kueri
    
    def find_admin(self, username, password):
        query = "SELECT * FROM Admin WHERE Username = %s AND password = %s"
        values = (username, password)
        
        myCursor = self.connection.cursor() 
        myCursor.execute(query, values)  # Eksekusi kueri dengan menggunakan variabel values
        myresult = myCursor.fetchall()   # Ambil hasil dari kueri

        return myresult 
    
    def registrasi(self, nama_user, gender, usia):
        query = "INSERT INTO Pengunjung (ID_Pengunjung, Nama_Pengunjung, Jenis_Kelamin, Umur) VALUES (NULL, %s, %s, %s)"
        values = (nama_user, gender, usia)

        myCursor = self.connection.cursor() 
        myCursor.execute(query, values) 

        self.connection.commit()

        return myCursor.lastrowid

    def add_wisata(self, nama_wisata, lokasi, deskripsi):
        query = "INSERT INTO Wisata (ID_Wisata, Nama_Wisata, Lokasi, Deskripsi) VALUES (NULL, %s, %s, %s)"
        values = (nama_wisata, lokasi, deskripsi)
        
        myCursor = self.connection.cursor()
        myCursor.execute(query, values)
        
        self.connection.commit()

        return myCursor.lastrowid
    
    def get_wisata(self, id_wisata = None):
        myCursor = self.connection.cursor()
        query  = "SELECT * FROM Wisata"
        myCursor.execute(query)
        return myCursor.fetchall()
    
    def update_wisata(self, id_wisata,  nama_wisata=None, lokasi=None, deskripsi=None):
        query = "UPDATE Wisata SET Nama_Wisata = %s, Lokasi = %s, Deskripsi = %s WHERE ID_Wisata = %s"
        values = (nama_wisata, lokasi, deskripsi, id_wisata)
        
        myCursor = self.connection.cursor()
        myCursor.execute(query, values)
        
        self.connection.commit() 
    
    def delete_wisata(self, id_wisata):
        query = "DELETE FROM Wisata WHERE ID_Wisata = %s"
        values = (id_wisata,)
        
        myCursor = self.connection.cursor()
        myCursor.execute(query, values)
        
        self.connection.commit()
    
    def search_wisata(self, search_query):
        myCursor = self.connection.cursor()
        query = "SELECT * FROM Wisata WHERE Nama_Wisata LIKE %s OR Lokasi LIKE %s OR Deskripsi LIKE %s"
        values = ('%' + search_query + '%', '%' + search_query + '%')
        myCursor.execute(query, values)
        
        return myCursor.fetchall()

    def get_sorted_wisata_ascending(self):
        myCursor = self.connection.cursor()
        query = "SELECT * FROM Wisata ORDER BY ID_Wisata ASC"
        myCursor.execute(query)
        
        return myCursor.fetchall()
    
    def get_sorted_wisata_descending(self):
        myCursor = self.connection.cursor()
        query = "SELECT * FROM Wisata ORDER BY ID_Wisata DESC"
        myCursor.execute(query)
        
        return myCursor.fetchall()