import sqlite3
from rand_class_datagen import generate_class_data

class_data = generate_class_data(10)

con = sqlite3.connect("ebookingclass.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS class_table (
    kode_kelas VARCHAR PRIMARY KEY,
    waktu VARCHAR,
    keterangan VARCHAR
)
""")

cursor.executemany(""" INSERT INTO class_table (kode_kelas, waktu, keterangan) VALUES (?, ?, ?)
""", class_data)

con.commit()