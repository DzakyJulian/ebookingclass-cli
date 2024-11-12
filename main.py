import os
import time
import sqlite3
from prettytable import from_db_cursor
from db import add_class, cancel_class
from gui import showInfoAlat, showPesanKelas, showDashboard

# Membuat koneksi ke database
connection = sqlite3.connect("ebookingclass.db")
cursor = connection.cursor()

# Fungsi login
def login():
    email = input("Masukkan email: ").strip()
    password = input("Masukkan password: ").strip()

    cursor.execute("SELECT * FROM accounts WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()
    
    if result:
        print("Login berhasil!")
        return True
    else:
        print("Login gagal! Email atau password salah.")
        return False

# Pengaturan batas dan jumlah percobaan login
max_attempts = 10
attempt_count = 0
block_time = 5

is_authenticated = False
while not is_authenticated:
    if attempt_count >= max_attempts:
        print(f"Terlalu banyak percobaan gagal! Coba lagi dalam {block_time} detik.")
        time.sleep(block_time)
        attempt_count = 0
        os.system("cls" if os.name == "nt" else "clear")

    if login():
        is_authenticated = True
        
        # Menampilkan data kelas
        cursor.execute("SELECT kode_kelas, waktu, keterangan FROM class_table")
        class_table = from_db_cursor(cursor)

# Menampilkan menu dan meminta input dari user
while True:
    showDashboard(class_table)  # Menampilkan dashboard

    # Menambahkan penjelasan tentang opsi yang tersedia
    print("\nPilih opsi yang tersedia:")
    print("1. Pesan kelas")
    print("2. Lihat informasi alat")
    print("3. Batalkan kelas")
    print("4. Keluar aplikasi")

    terminal_inp = input("Pilih opsi (1/2/3/4): ")

    if terminal_inp == '1':
        showPesanKelas()  # Fungsi untuk pesan kelas
    elif terminal_inp == '2':
        showInfoAlat()  # Fungsi untuk melihat informasi alat
    elif terminal_inp == '3':
        kode_kelas = input("Masukkan kode kelas yang ingin dibatalkan: ").strip()
        result = cancel_class(kode_kelas)  # Fungsi untuk membatalkan kelas
        print(result)

        # Memuat ulang data kelas terbaru setelah pembatalan
        cursor.execute("SELECT kode_kelas, waktu, keterangan FROM class_table")
        class_table = from_db_cursor(cursor)

    elif terminal_inp == '4':
        print("Terima kasih telah menggunakan aplikasi!")  # Pesan keluar
        break  # Keluar dari loop utama

    else:
        print("Opsi tidak valid. Silakan pilih 1, 2, 3, atau 4.")  # Penanganan input yang tidak valid


# Dzaky julian testing
