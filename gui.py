import os
from prettytable import PrettyTable

# Menampilkan informasi alat
def showInfoAlat():
    os.system("cls" if os.name == "nt" else "clear")
    alat_table = PrettyTable()
    alat_table.field_names = ["Alat", "Jumlah", "Status"]
    alat_table.add_row(["Laptop", "10", "Tersedia"])
    alat_table.add_row(["Projector", "5", "Tersedia"])
    alat_table.add_row(["Whiteboard", "3", "Tidak Tersedia"])
    print(alat_table)
    input("\nTekan Enter untuk kembali ke menu utama...")

# Menampilkan pesan kelas
def showPesanKelas():
    os.system("cls" if os.name == "nt" else "clear")
    print("Masukkan kode kelas yang ingin dipesan:")
    kode_kelas = input("> ")
    print(f"Pesanan kelas {kode_kelas} berhasil!")
    input("\nTekan Enter untuk kembali ke menu utama...")

# Menampilkan dashboard
def showDashboard(class_table):
    os.system("cls" if os.name == "nt" else "clear")
    print("==============================================================")
    print("|                     E-Booking Class                        |")
    print("|                       [ Dashboard ]                        |")
    print("==============================================================")
    print(class_table)
