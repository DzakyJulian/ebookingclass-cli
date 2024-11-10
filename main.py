import os
import time
import sqlite3
from prettytable import from_db_cursor
from tables import alat_table

# Koneksi ke database
connection = sqlite3.connect("ebookingclass.db")
cursor = connection.cursor()

def login():
    # global email, password
    email = input("Masukkan email: ").strip()
    password = input("Masukkan password: ").strip()
    
    cursor.execute("SELECT * FROM accounts WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()
    
    if result:
        print("==============================================================")
        print("|                    !LOGIN BERHASIL!                        |")
        print("|                     SELAMAT DATANG                         |")
        print("==============================================================")
        return True
    else:
        print("==============================================================")
        print(" |                       LOGIN GAGAL!                        |")
        print(" |       Email atau password salah, silahkan coba lagi       |")
        print("==============================================================")
        return False

max_attempts = 10
attempt_count = 0
block_time = 5 

is_authenticated = False
while not is_authenticated:
   
    if attempt_count >= max_attempts:
        print(f"Terlalu banyak percobaan gagal! Coba lagi dalam 5 detik.")
        time.sleep(block_time)  
        attempt_count = 0  
        print("-"*30)
        os.system("cls" if os.name == "nt" else "clear")

    # Memanggil fungsi login dan cek autentikasi
    if login():
        is_authenticated = True
        cursor.execute("SELECT kode_kelas, waktu, keterangan FROM class_table")
        class_table = from_db_cursor(cursor)
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
        attempt_count += 1  # Tambahkan hitungan percobaan jika login gagal

       
            
