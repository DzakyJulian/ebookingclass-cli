import os   # os: untuk operasi sistem seperti membersihkan terminal
import time # time: untuk pengaturan waktu tunggu (delay) saat gagal login
import sqlite3  # sqlite3: untuk menghubungkan dan beroperasi pada database SQLite
from prettytable import from_db_cursor  # prettytable: untuk menampilkan data tabel dari database dengan format yang rapi
from gui import showInfoAlat, showPesanKelas, showDashboard # gui: modul GUI khusus yang menyediakan fungsi untuk menampilkan elemen antarmuka seperti info alat, pesan kelas, dan dashboard

# Membuat koneksi ke database
connection = sqlite3.connect("ebookingclass.db")
cursor = connection.cursor()

def login():
    # Fungsi untuk autentikasi pengguna melalui email dan password
    # Input dan validasi terhadap tabel accounts di database
    email = input("Masukkan email: ").strip()
    password = input("Masukkan password: ").strip()

    # Mengecek kredensial pengguna di tabel accounts
    cursor.execute("SELECT * FROM accounts WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()
    
    if result:
        # Login berhasil jika ditemukan data yang cocok
        print("==============================================================")
        print("|                    !LOGIN BERHASIL!                        |")
        print("|                     SELAMAT DATANG                         |")
        print("==============================================================")
        return True
    else:
        # Pesan error jika login gagal
        print("==============================================================")
        print(" |                       LOGIN GAGAL!                        |")
        print(" |       Email atau password salah, silahkan coba lagi       |")
        print("==============================================================")
        return False

# Pengaturan batas dan jumlah percobaan login
max_attempts = 10
attempt_count = 0
block_time = 5  # Waktu tunggu setelah percobaan maksimal tercapai

is_authenticated = False
while not is_authenticated:
   
    if attempt_count >= max_attempts:
        # Pesan blokir jika terlalu banyak percobaan gagal
        print(f"Terlalu banyak percobaan gagal! Coba lagi dalam 5 detik.")
        time.sleep(block_time)  
        attempt_count = 0
        print("-"*30)
        os.system("cls" if os.name == "nt" else "clear")

    # Memanggil fungsi login dan cek autentikasi
    if login():
        is_authenticated = True  # Status login berhasil
        cursor.execute("SELECT kode_kelas, waktu, keterangan FROM class_table")
        class_table = from_db_cursor(cursor)
        
        # Menambahkan opsi interaksi ke tabel
        class_table.add_row(['','',''], divider=True)
        class_table.add_row(['Pesan Kelas (1)','Ingfo Alat Perlengkapan(2)','Exit(3)'])

        while True:
                terminal_inp = 0
                        
                if (terminal_inp == 0):
                    showDashboard()

                if (terminal_inp == 1):
                    showPesanKelas()

                if (terminal_inp == 2):
                    showInfoAlat()
    else:
        # Menambah hitungan percobaan jika login gagal
        attempt_count += 1
