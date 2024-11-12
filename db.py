import sqlite3

def add_class(kode_kelas, waktu, keterangan):
    connection = sqlite3.connect("ebookingclass.db")
    cursor = connection.cursor()

    # Menambahkan kelas baru ke database
    cursor.execute("INSERT INTO class_table (kode_kelas, waktu, keterangan) VALUES (?, ?, ?)",
                   (kode_kelas, waktu, keterangan))
    connection.commit()
    connection.close()

def cancel_class(kode_kelas):
    connection = sqlite3.connect("ebookingclass.db")
    cursor = connection.cursor()

    # Cek apakah kelas yang ingin dibatalkan ada
    cursor.execute("SELECT * FROM class_table WHERE kode_kelas = ?", (kode_kelas,))
    class_exists = cursor.fetchone()

    if class_exists:
        # Hapus kelas dari database
        cursor.execute("DELETE FROM class_table WHERE kode_kelas = ?", (kode_kelas,))
        connection.commit()
        connection.close()
        return f"Kelas dengan kode {kode_kelas} berhasil dibatalkan."
    else:
        connection.close()
        return f"Kelas dengan kode {kode_kelas} tidak ditemukan."
