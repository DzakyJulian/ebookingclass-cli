import os
import sqlite3
from prettytable import from_db_cursor
from tables import alat_table

connection = sqlite3.connect("ebookingclass.db")
cursor = connection.cursor()
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
