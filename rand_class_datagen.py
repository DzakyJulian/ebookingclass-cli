import random  # Mengimpor modul random untuk menghasilkan angka acak
from datetime import datetime, timedelta # Mengimpor modul datetime dan timedelta untuk bekerja dengan tanggal dan waktu

def generate_class_data(num_records):
    data = []  # Daftar kosong untuk menyimpan data kelas
    base_date = datetime(2024, 11, 12, 8, 0)  # Tanggal dan waktu dasar untuk kelas
    
    for i in range(num_records): # Loop untuk menghasilkan data kelas sebanyak num_records
        class_code = f"20.4B.04.{str(i+1).zfill(3)}"   # Membuat kode kelas dengan format tertentu

        random_minutes = random.randint(0, 60 * 24 * 7) # Menghasilkan angka acak dalam rentang menit selama seminggu
        class_datetime = base_date + timedelta(minutes=random_minutes) # Menghitung tanggal dan waktu kelas dengan menambahkan random_minutes ke base_date
        class_datetime_str = class_datetime.strftime("%A %d %B %Y, %H:%M") # Mengonversi class_datetime menjadi string dengan format yang lebih mudah dibaca

        status = random.choice(["Tersedia", "Tidak Tersedia"])  # Menghasilkan status acak untuk kelas

        data.append((class_code, class_datetime_str, status)) # Menambahkan tuple (class_code, class_datetime_str, status) ke dalam daftar data

    return data # Mengembalikan daftar data kelas

class_data = generate_class_data(10) # Memanggil fungsi generate_class_data untuk menghasilkan 10 catatan kelas

print(class_data) # Mencetak hasil data kelas yang dihasilkan