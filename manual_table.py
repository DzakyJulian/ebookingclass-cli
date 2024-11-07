import os
from prettytable import PrettyTable

# inisialisasi PrettyTable
table = PrettyTable()
table.field_names = ["Kode Kelas", "Waktu", "Keterangan"]

# list kelas
kelas = [
    ["20.4B.04.002", "Kamis 12 November 2024, 12:35", "Tersedia"],
    ["20.4E.02.006", "Rabu 12 November 2024, 12:35", "Penuh"]
]

# masukin semua kelas ke dalem tabel pake for loop
for i in range(0, len(kelas)):
    table.add_row(kelas[i])
    
os.system("cls")

print("==============================================================")
print("|                     E-Booking Class                        |")
print("|                      [ Dashboard]                          |")
print("==============================================================")
print(table)
