import os
from tables import alat_table

def showInfoAlat():
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

def showPesanKelas():
    os.system("cls")
    print(terminal_inp)
    print("==============================================================")
    print("|                     E-Booking Class                        |")
    print("|                     [ Pesan Kelas ]                        |")
    print("==============================================================")
    inp = int(input("Masukkan kode kelas yang ingin dipesan > "))
    terminal_inp = inp
    
def showDashboard():
    os.system("cls")
    print(terminal_inp)
    print("==============================================================")
    print("|                     E-Booking Class                        |")
    print("|                      [ Dashboard]                          |")
    print("==============================================================")
    print(class_table)
    inp = int(input("> "))
    terminal_inp = inp