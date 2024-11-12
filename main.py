import os
import time
import sqlite3
from prettytable import from_db_cursor
from tables import alat_table

# Koneksi ke database
connection = sqlite3.connect("ebookingclass.db")
cursor = connection.cursor()

def login():
    # Meminta input email dan password dari pengguna
    email = input("Masukkan email: ").strip()
    password = input("Masukkan password: ").strip()

    # Mengecek kredensial di tabel accounts pada database
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

# Variabel untuk batas dan jumlah percobaan login
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
                    os.system("cls")
                    print(terminal_inp)
                    print("==============================================================")
                    print("|                     E-Booking Class                        |")
                    print("|                      [ Dashboard]                          |")
                    print("==============================================================")
                    print(class_table)
                    inp = int(input("> "))
                    terminal_inp = inp

                if (inp == 1):
                    os.system("cls")
                    print(terminal_inp)
                    print("==============================================================")
                    print("|                     E-Booking Class                        |")
                    print("|                     [ Pesan Kelas ]                        |")
                    print("==============================================================")
                    inp = int(input("Masukkan kode kelas yang ingin dipesan > "))
                    terminal_inp = inp

                if (inp == 2):
                    os.system("cls")
                    print(terminal_inp)
                    print("==============================================================")
                    print("|                     E-Booking Class                        |")
                    print("|          [ Informasi Alat Perlengkapan Kelas ]             |")
                    print("==============================================================")
                    alat_table.add_row(['','','',''], divider=True)
                    alat_table.add_row(['Kembali (1)','Request Alat (2)','','Exit(3)'])
                    print(alat_table)
                    inp = int(input("> "))
                    terminal_inp = inp
    else:
        # Menambah hitungan percobaan jika login gagal
        attempt_count += 1
