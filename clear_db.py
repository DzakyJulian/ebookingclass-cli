import sqlite3

con = sqlite3.connect("ebookingclass.db")
cursor = con.cursor()

cursor.execute("DELETE FROM class_table")
con.commit()